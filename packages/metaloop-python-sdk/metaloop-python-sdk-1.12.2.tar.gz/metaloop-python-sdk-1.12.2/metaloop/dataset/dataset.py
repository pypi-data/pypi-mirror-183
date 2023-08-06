import json
import logging
import os.path
import time
from typing import List, Optional, Any, TYPE_CHECKING

from s3transfer.constants import GB
from tqdm import tqdm
from urllib.parse import urlparse

from metaloop.client.cloud_storage import CloudConfig, CloudClient, Item
from metaloop.client.download_helper import DownloadHelper
from metaloop.utils.file_helper import *
from metaloop.exception import ResourceNotExistError, InvalidParamsError, InternalServerError

if TYPE_CHECKING:
    from metaloop.client.mds import MDS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DATASET_SUMMARY_TEMPLATE = """
===================================================================
######################## Dataset Summary ##########################
name:              {}
space:             {}
create_user:       {}
create_time:       {}
data_type:         {}
tags:              {}
-------------------------------------------------------------------
version:           {}
import_status:     {}
clean_status:      {}
data_count:        {}
annotation_status: {}
comment:           {}
"""


class DatasetMeta:
    def __init__(self,
                 mds: "MDS",
                 name: str,
                 data_type: str,
                 space: str,
                 tags: Optional[List[str]],
                 created_user: Optional[str],
                 create_timestamp: Optional[int],
                 versions: Optional[Dict[int, str]],
                 source: Optional[str] = "",
                 meta_comment: Optional[str] = ""):
        self._x_api = mds.x_api
        self._name = name
        self._data_type = data_type
        self._space = space
        self._source = source
        self._tags = tags
        self._created_user = created_user
        self._meta_comment = meta_comment
        self._create_timestamp = create_timestamp
        self._versions = versions

    @property
    def versions(self):
        return self._versions


class Dataset(DatasetMeta):
    def __init__(self,
                 mds: "MDS",
                 name: str,
                 data_type: str,
                 space: str,
                 dataset_id: str,
                 version: int,
                 tags: Optional[List[str]] = None,
                 created_user: Optional[str] = "",
                 create_timestamp: Optional[int] = 0,
                 versions: Optional[Dict[int, str]] = None,
                 source: Optional[str] = "",
                 meta_comment: Optional[str] = "",
                 comment: Optional[str] = "",
                 data_count: Optional[int] = 0,
                 annotation_status: Optional[int] = 0,
                 last_import_status: Optional[int] = 0,
                 last_data_clean_status: Optional[int] = 0,
                 attachment_url: Optional[str] = ""
                 ):
        super().__init__(
            mds,
            name,
            data_type,
            space,
            tags,
            created_user,
            create_timestamp,
            versions,
            source,
            meta_comment)

        self._id = dataset_id
        self._comment = comment
        self._data_count = data_count
        self._version = version
        self._annotation_status = annotation_status
        self._last_import_status = last_import_status
        self._last_data_clean_status = last_data_clean_status
        self._attachment_url = attachment_url

        self.iter_batch_size = 128
        self.iter_current_start = 0
        self.iter_current_end = 0
        self.iter_current_object = []

    @property
    def id(self):
        return self._id

    def create_version(
            self,
            inherited_version_number: Optional[int] = None,
            comment: Optional[str] = "",
    ) -> None:
        """Create a new version of the dataset, optional inherit a previous version or not.

        if you want to inherit the data from a previous version, then set the
        inherited_version_number to that version.

        Arguments:
            inherited_version_number: The number of inherited version.
            comment: Comment of the new version.

        """
        post_data = {
            "name": self._name,
            "data_type": self._data_type,
            "comment": comment,
        }

        info = self._x_api.create_dataset(post_data)

        dataset_id = info["id"]
        version = info["version"]

        if inherited_version_number is not None and inherited_version_number > -1:
            self.checkout(inherited_version_number)
            if self._data_count > 0:
                self._inherit_import(dataset_id, inherited_version_number)

        self._versions[version] = dataset_id
        self._id = dataset_id
        self._comment = comment
        self._version = version
        self._annotation_status = 0
        self._last_import_status = 0
        self._last_data_clean_status = 0

    def delete_version(
            self,
            version_number: Optional[int] = None
    ) -> None:
        """Delete a version of the dataset.

        Arguments:
            version_number: Version number of the dataset.

        """
        if not version_number:
            version_number = self._version
        elif version_number not in self._versions:
            raise ResourceNotExistError(resource="version", identification=version_number)

        dataset_id = self._versions[version_number]

        self._x_api.delete_dataset(dataset_id)
        self._versions.pop(version_number)

        if len(self._versions) == 0:
            self._id = ""
            self._comment = ""
            self._version = -1
            self._annotation_status = 0
            self._last_import_status = 0
            self._last_data_clean_status = 0
        elif version_number == self._version:
            max_version = max(self._versions.keys())
            self.checkout(max_version)

    def checkout(self, version_number: int) -> None:
        """Checkout to a version by the given version_number.

        Arguments:
            version_number: Version number of the dataset.

        Raises:
            ResourceNotExistError: The dataset doesn't contains the specified version.

        """

        if version_number not in self._versions:
            raise ResourceNotExistError(resource="version", identification=version_number)

        info = self._x_api.get_version(self._versions[version_number])

        self._id = info["id"]
        self._comment = info["comment"]
        self._data_count = info["data_count"]
        self._version = info["version"]
        self._annotation_status = info["annotation_status"]
        self._last_import_status = info["last_import_status"]
        self._last_data_clean_status = info["last_data_clean_status"]
        self._attachment_url = info["attachment_url"] if "attachment_url" in info else ""

    def summary(self) -> None:
        """Print the summary of the dataset.

        """
        if not self._id:
            return
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self._create_timestamp * 1e-3))
        space = self._space if self._space else "个人"
        print(DATASET_SUMMARY_TEMPLATE.format(self._name, space, self._created_user, date_time, self._data_type,
                                              self._tags, self._version, self._last_import_status,
                                              self._last_data_clean_status, self._data_count,
                                              self._annotation_status, self._comment))

    def __len__(self):
        return self._data_count

    def __getitem__(self, index):
        if index < 0:
            index = self._data_count + index
        if index >= self._data_count:
            raise IndexError
        if index >= self.iter_current_start and index < self.iter_current_end:
            return self.iter_current_object[index - self.iter_current_start]
        try:
            response = self._x_api.list_objects(self._id, index, self.iter_batch_size)
            items = response["data"]
        except IndexError as error:
            raise ResourceNotExistError(resource="dataset", identification=self._id) from error

        self.iter_current_start = index
        self.iter_current_end = index + len(items)
        self.iter_current_object = items

        return self.iter_current_object[index - self.iter_current_start]

    def import_data(
            self,
            file_path: str,
            import_type: Optional[str] = "none",
            storage_type: Optional[str] = "local",
            append_path: Optional[str] = "",
            transcode: Optional[bool] = False
    ) -> None:
        """Upload and import data to dataset from local.

        Arguments:
            file_path: Local file path, can be either file or directory.
            import_type: Import type of local data, includes
                "none", "evalmodels", "pre_annotation", "standard", "multiform".
            storage_type: Cloud storage type of imported data, includes:

                1. "local": MetaLoop default local object storage;
                2. "cos": Tencent Cloud Object Storage (COS).

            append_path: The specified path to store data in the object storage (without bucket).
            transcode: Whether converse format of data, only used for video.

        """
        if not file_path:
            raise InvalidParamsError(param_name="file_path", param_value=file_path)

        if storage_type not in {"local", "cos"}:
            raise InvalidParamsError(param_name="storage_type", param_value=storage_type)

        if append_path:
            append_path = self._x_api.get_dataset_path(self._id, append_path)

        print(f"upload file to server, please wait...")

        if storage_type == "cos":
            if not os.path.isdir(file_path):
                file_type = get_file_type(file_path)[1]
                if file_type == FileTypeZip:
                    raise InvalidParamsError(message="Tencent COS uploading do not support compressed file")
                upload_id = self._upload_file(file_path, storage_type, append_path)
            else:
                upload_prefix = append_path if append_path else self._id
                upload_id = self._upload_files(file_path, storage_type, upload_prefix)
            task_type = "cos"

        elif os.path.isfile(file_path) and os.path.getsize(file_path) > 1 * GB:
            upload_id = self._upload_file(file_path, storage_type, append_path)
            task_type = "object_storage"

        elif os.path.isdir(file_path):
            if append_path:
                raise InvalidParamsError(message="Directory uploading do not support append_path, please try with zip")
            upload_id = self._upload_files(file_path, storage_type, append_path)
            task_type = "object_storage"

        else:
            upload_id = self._post_multipart_formdata(file_path)
            task_type = "local_file"

        print(f"upload file '{file_path}' to server success, upload_id: '{upload_id}'")

        post_data: Dict[str, Any] = {
            "transcode": transcode,
            "create_timestamp": int(time.time() * 1000),
            "data_type": self._data_type,
            "data_url": [
                upload_id
            ],
            "import_type": import_type,
            "task_type": task_type,
            "append_path": append_path
        }

        self._x_api.post_import(self._id, post_data)

        print(f"import data to dataset start, please wait...")

        with tqdm(total=100) as pbar:
            self._validate_import(pbar)

        self.checkout(self._version)

    def export_data(
            self,
            file_path: str,
            storage_type: Optional[str] = "local",
            export_path: Optional[List[str]] = None
    ) -> None:
        """Export data to local file from dataset.

        Arguments:
            file_path: File path of exported data.
            storage_type: Source of exported data, includes:

                1. "local": MetaLoop default local object storage;
                2. "external": Tencent Cloud Object Storage (COS).

            export_path: Export data from the specific path[s].

        """
        if storage_type not in {"local", "external"}:
            raise InvalidParamsError(param_name="storage_type", param_value=storage_type)

        if storage_type == "external":
            self._get_cloud_storage_config('', storage_type=storage_type)
        self.checkout(self._version)
        export_type = "annotation_uri" if self._annotation_status == 2 else "uri_json_standard"

        post_data: Dict[str, Any] = {
            "dataset_id": self._id,
            "export_type": export_type,
            "storage_type": storage_type,
            "task_type": "shared_links",
        }
        if export_path:
            if isinstance(export_path, list):
                path = [self._x_api.get_dataset_path(self._id, path) for path in export_path]
                post_data["export_path"] = path
            else:
                raise InvalidParamsError(message=f"export_path value type should be list")

        self._x_api.post_export(self._id, post_data)
        print("export data start, please wait...")

        with tqdm(total=100) as pbar:
            download_url = self._validate_export(pbar)

        catalog = self._x_api.get_export_catalog(download_url)

        print("download data from server, please wait...")
        time.sleep(0.3)

        if not os.path.exists(file_path):
            os.makedirs(file_path, 0o0775)

        file_writer = open(os.path.join(file_path, "output.json.tmp"), "w")
        download_helper = DownloadHelper(self._x_api)

        count = 0
        for obj in catalog:
            count += 1
            ex = False
            image_path = obj["image_path"] if "image_path" in obj else ""

            if "external_url_image" in obj:
                # /{bucket}/{path}/{to}/{object}.ext
                url = obj["external_url_image"]

                items = url.strip("/").split("/")
                if len(items) < 2:
                    continue

                s3_config = self._get_cloud_storage_config(items[0], storage_type=storage_type)

                file_name = download_helper.download_s3_file(
                    self._download_file,
                    identifier=s3_config.identifier,
                    bucket=items[0],
                    url=url,
                    file_path=file_path,
                    image_path=image_path
                )
                obj["url_image"] = file_name
                ex = True

            if not ex:
                # {endpoint}/{bucket}/{path}/{to}/{object}.ext
                url = str(obj["url_image"])
                file_name = download_helper.download_http_file(
                    self._download_http_file,
                    url=url,
                    file_path=file_path,
                    image_path=image_path
                )
                obj["url_image"] = file_name

            body = json.dumps(obj, ensure_ascii=False)
            file_writer.write(body)
            file_writer.write("\n")
            if not count % 128:
                file_writer.flush()

        download_helper.force_submit()
        download_helper.wait()

        file_writer.flush()
        file_writer.close()
        os.rename(os.path.join(file_path, "output.json.tmp"), os.path.join(file_path, "output.json"))

    def merge(
            self,
            dataset_ids: List[str]
    ):
        """Merge dataset to current dataset
        Arguments:
            dataset_ids: The IDs of dataset to be merged

        """
        if not dataset_ids:
            raise ResourceNotExistError(message="dataset_ids is empty")

        self._x_api.merge_dataset(self._id, dataset_ids)
        self.checkout(self._version)

    def _get_dataset(
            self,
            dataset_id: str
    ) -> Dict[str, Any]:
        if not dataset_id:
            raise ResourceNotExistError(resource="dataset", identification=dataset_id)

        try:
            response = self._x_api.get_version(dataset_id)
            info = response.json()["data"][0]
        except IndexError as error:
            raise ResourceNotExistError(resource="dataset", identification=dataset_id) from error

        return info

    def _inherit_import(
            self,
            dataset_id: str,
            version_number: int
    ) -> None:
        try:
            version_id = self._versions[version_number]
        except KeyError as error:
            raise ResourceNotExistError(resource="version", identification=version_number) from error

        post_data: Dict[str, Any] = {
            "create_timestamp": int(time.time() * 1000),
            "data_type": self._data_type,
            "data_url": [
                version_id
            ],
            "task_type": "dataset"
        }

        self._x_api.post_import(dataset_id, post_data)
        self._validate_import()

    def _validate_import(
            self,
            pbar: Optional[tqdm] = None
    ) -> None:
        last_progress = 0
        while True:
            info = self._x_api.get_import_status(self._id)
            progress = info["progress"]
            if progress == -1:
                raise InternalServerError(message=info["message"])
            if pbar:
                pbar.update(progress - last_progress)
            if progress >= 100:
                if pbar:
                    print(f"import data finished")
                break
            last_progress = progress
            time.sleep(1)

    def _validate_export(
            self,
            pbar: Optional[tqdm] = None
    ) -> str:
        last_progress = 0
        time.sleep(0.3)
        while True:
            info = self._x_api.get_export_status(self._id)
            progress = info["progress"]
            if progress == -1:
                raise InternalServerError(message=info["message"])
            if pbar:
                pbar.update(progress - last_progress)
            if progress >= 100:
                return info["data_url"]
            last_progress = progress
            time.sleep(1)

    def _upload_file(
            self,
            file_path: str,
            storage_type: str,
            upload_prefix: Optional[str] = ""
    ) -> str:
        bucket = self._get_bucket(storage_type)
        s3_config = self._get_cloud_storage_config("", storage_type)
        if not bucket:
            bucket = s3_config.default_bucket
        return CloudClient.upload_file(s3_config.identifier, bucket, file_path, upload_prefix)

    def _upload_files(
            self,
            file_path: str,
            storage_type: str,
            upload_prefix: Optional[str] = ""
    ) -> str:
        s3_config = self._get_cloud_storage_config("", storage_type)

        bucket = self._get_bucket(storage_type)
        if not bucket:
            bucket = s3_config.default_bucket

        return CloudClient.upload_files_parallel(s3_config.identifier, bucket, file_path, upload_prefix)

    @staticmethod
    def _download_file(
            **kwargs
    ) -> Tuple[str, Item]:
        key, file_name, obj_url = Dataset._get_download_info(
            kwargs["url"],
            kwargs["file_path"],
            kwargs["image_path"]
        )
        return kwargs["identifier"], Item(kwargs["bucket"], key, file_name, obj_url)

    @staticmethod
    def _download_http_file(
            **kwargs
    ) -> Item:
        _, file_name, obj_url = Dataset._get_download_info(
            urlparse(kwargs["url"]).path,
            kwargs["file_path"],
            kwargs["image_path"]
        )
        return Item("", kwargs["url"], file_name, obj_url)

    @staticmethod
    def _get_download_info(
            url: str,
            file_path: str,
            image_path: str
    ) -> Tuple[str, str, str]:
        _, key = get_bucket_and_key(url)

        if not image_path:
            image_path = get_user_origin_path(key)

        if not file_path or image_path.find("/") < 0:
            image_path = os.path.join("abaddon", image_path)

        file_name = os.path.join(file_path, image_path.strip("/"))

        if not os.path.exists(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name), 0o0755)

        while file_path.endswith('/'):
            file_path = file_path[:-1]

        obj_url = file_name[len(file_path) + 1:]

        return key, file_name, obj_url

    def _download_files(
            self,
            bucket: str,
            prefix: str,
            file_path: str
    ) -> str:
        s3_config = self._get_cloud_storage_config(bucket)
        return CloudClient.download_files_parallel(s3_config.identifier, bucket, prefix, file_path)

    def _get_cloud_storage_config(
            self,
            name: str,
            storage_type: Optional[str] = ""
    ) -> CloudConfig:
        if not name:
            name = storage_type

        if not CloudClient.find_s3_config(name):
            info = self._x_api.get_authorized_s3_config(name, storage_type)
            identifier = info["name"]
            endpoint = info["endpoint"]
            access_key = info["access_key"]
            secret_key = info["secret_key"]
            default_bucket = info["bucket"]

            CloudClient.set_s3_config(identifier, endpoint, access_key, secret_key, default_bucket)
            if name != default_bucket:
                CloudClient.set_s3_config(default_bucket, endpoint, access_key, secret_key, default_bucket)
        else:
            identifier = name

        return CloudClient.find_s3_config(identifier)

    def _get_bucket(
            self,
            storage_type: str
    ) -> str:
        if self._space != "":
            space = self._x_api.get_space(self._space)

            if storage_type == "external" and "cloud_bucket" in space:
                return space["cloud_bucket"]
            elif storage_type == "local" and "bucket" in space:
                return space["bucket"]

        return ""

    def _post_multipart_formdata(
            self,
            file_path: str,
    ) -> str:
        post_data: Dict[str, Any] = {}

        with open(file_path, "rb") as fp:
            file_name = os.path.basename(file_path)
            file_type = get_file_type(file_path)

            post_data["file"] = (file_name, fp, file_type[0])
            post_data["file_type"] = file_type[1]

            upload_id = self._x_api.post_multipart_formdata(post_data)

        return upload_id

    def _get_stream_data(
            self,
            url: str,
            file_path: str
    ) -> str:
        if url.startswith("http://"):
            file_name = url[url.index("http://") + 7:]
        elif url.startswith("https://"):
            file_name = url[url.index("https://") + 8:]
        else:
            file_name = url

        index = file_name.find("/")
        if index > -1:
            file_name = os.path.join(file_path, file_name[index + 1:])
        else:
            file_name = os.path.join(file_path, file_name)

        if not os.path.exists(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name), 0o0755)

        self._x_api.get_stream_data(url, file_name)

        return url[index + 8:]
