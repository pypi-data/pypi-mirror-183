import hashlib
import json
import os
import re
import warnings
from abc import ABC, abstractmethod
from typing import Dict, List, Literal, Union

import boto3
import pandas as pd
from PIL import Image
from tqdm import tqdm


class BaseDataInterface(ABC):
    """
    `BaseDataInterface` is an abstract class for data interface.
    """

    def __init__(self, use_memory: bool = False):
        """
        Initialize the data interface.
        @param use_memory:
        """
        self._keys: List[str] = []
        self._memory: Dict[str, Union[dict, pd.DataFrame, Image.Image]] = {}

    @abstractmethod
    def __getitem__(self, key):
        """

        @param key:
        @return:
        """
        raise NotImplementedError

    def __len__(self):
        return len(self.keys())

    def keys(self):
        return self._keys

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, new_memory) -> None:
        """
        Set the memory.
        @type new_memory: Dict[str, Union[dict, pd.DataFrame, Image.Image]]
        """
        warnings.warn("You cannot set data directly. Use `use_memory` option instead.")
        _ = new_memory


class ExternalDataInterface(BaseDataInterface, ABC):
    """
    `ExternalDataInterface` is a class that loads data from external storage.
    """

    DOWNLOAD_ROOT = ".doodlin_ai/data/"

    def __init__(self, use_memory: bool = False):
        """

        @param use_memory:
        """
        super().__init__()


class S3DataInterface(ExternalDataInterface):
    """
    `S3DataInterface` is a class that can interface data from s3.
    It can download data from s3 and store it in memory.
    It can also download data from s3 and store it in local disk.
    """

    def __init__(
        self,
        bucket_name: str = "greeting-datasets",
        prefix: str = "/",
        regex: str = ".*",
        download: Literal["auto", "force", "none"] = "auto",
        use_checksum: bool = False,
        use_memory: bool = False,
    ):
        """
        `__init__` initializes `S3DataInterface`.
        @param bucket_name:
            bucket name to download data from.
        @param prefix:
            prefix to download data from.
        @param regex:
            regex to filter data.
        @param download:
            download data from s3.
        @param use_checksum:
            use checksum to check if file is already downloaded.
        @param use_memory:
            store data in memory.
        """
        super().__init__()

        self.s3 = boto3.resource("s3")
        self.bucket = self.s3.Bucket(bucket_name)
        self.DOWNLOAD_ROOT = os.path.join(self.DOWNLOAD_ROOT, bucket_name)
        self.objs = self.bucket.objects.filter(Prefix=prefix)
        self._keys = [
            obj.key for obj in self.objs if re.match(regex, os.path.basename(obj.key))
        ]
        self._memory = {}
        if download in ("auto", "force"):
            self.download(
                force_download=(download == "force"), use_checksum=use_checksum
            )

        if use_memory:
            for key in self.keys():
                self._memory[key] = self[key]

    def download(
        self, force_download: bool = False, use_checksum: bool = False
    ) -> None:
        """
        function `download` downloads data from s3.

        @param force_download:
            force download even if file exists.
        @param use_checksum:
            use checksum to check if file is already downloaded.
        @return: None
        """
        pbar = tqdm(self.keys(), miniters=10)
        for i, key in enumerate(pbar):
            # if exists, check its checksum.
            # if checksum is different, download it.
            if (
                os.path.exists(os.path.join(self.DOWNLOAD_ROOT, key))
                and not force_download
            ):
                if use_checksum:
                    f = open(os.path.join(self.DOWNLOAD_ROOT, key), "rb")
                    checksum = hashlib.md5(f.read()).hexdigest()
                    s3_checksum = self.bucket.Object(key).e_tag[1:-1]
                    if checksum == s3_checksum:
                        continue
                else:
                    continue  # pragma: no cover
                    # Reason: Python coverage cannot detect this line.
                    # Check this https://github.com/nedbat/coveragepy/issues/198

            os.makedirs(
                os.path.join(self.DOWNLOAD_ROOT, os.path.dirname(key)), exist_ok=True
            )
            pbar.set_description(
                f'Downloading {"/".join(key.split("/")[-2:]):>30}'
                f'{"." * (i % 4)}{" " * (4 - i % 4)}'
            )

            self.bucket.download_file(key, os.path.join(self.DOWNLOAD_ROOT, key))

    def __getitem__(self, key: str) -> Union[dict, pd.DataFrame, Image.Image]:
        """

        @param key:
        @return:
        """
        # if downloaded file exists, open file and return it.
        # else get it from s3.
        if key in self._memory.keys():
            return self._memory[key]
        else:
            if key.endswith(".json"):
                if os.path.exists(os.path.join(self.DOWNLOAD_ROOT, key)):
                    with open(os.path.join(self.DOWNLOAD_ROOT, key)) as f:
                        return json.load(f)
                else:
                    return json.loads(
                        self.bucket.Object(key).get()["Body"].read().decode("utf-8")
                    )
            elif key.endswith(".csv"):
                if os.path.exists(os.path.join(self.DOWNLOAD_ROOT, key)):
                    return pd.read_csv(os.path.join(self.DOWNLOAD_ROOT, key))
                else:
                    return pd.read_csv(self.bucket.Object(key).get()["Body"])
            elif key.endswith(".jpg"):
                if os.path.exists(os.path.join(self.DOWNLOAD_ROOT, key)):
                    return Image.open(os.path.join(self.DOWNLOAD_ROOT, key))
                else:
                    return Image.open(self.bucket.Object(key).get()["Body"])
            else:
                raise NotImplementedError(f"Not supported file type: {key}")
