import os
import sys
import time
from concurrent.futures import ALL_COMPLETED
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from concurrent.futures import wait

import tqdm
import uuid
import enum
import copy
import hashlib
import logging
import requests
import pandas as pd

from io import BytesIO
from io import StringIO
from typing import List
from datetime import datetime
from prettytable import prettytable
from retry import retry

from .client import BaseRemoteClient


logger = logging.getLogger()


class CaseStatusEnum(enum.Enum):
    waiting = 'waiting'
    uploading = 'uploading'
    uploaded = 'uploaded'
    loading = 'loading'
    finished = 'finished'
    failed = 'failed'


class CaseTypeEnum(enum.Enum):
    characteristic_exposure = 'characteristic_exposure'
    characteristic_return = 'characteristic_return'
    characteristic_covariance = 'characteristic_covariance'
    characteristic_idiosyncratic_variance = 'characteristic_idiosyncratic_variance'
    characteristic_scale = 'characteristic_scale'


class CheckCaseType:
    characteristic_exposure = ["date", "characteristic", 'exposure', "code", "type"]
    characteristic_return = ["date", "characteristic", "return", "type"]
    characteristic_covariance = ["date", "source", "target", "cov"]
    characteristic_idiosyncratic_variance = ["date", "code", "var"]
    characteristic_scale = ["date", "code", "scale"]


class Uploader(object):
    max_workers = 5
    print_time_sleep = 10

    def __init__(self, client: BaseRemoteClient):
        self.client = client
        self.case_name = None
        self.file_list = None
        self.file_uploader_list = None

    def upload(self, case_name: str, file_list: list, daemon=True):
        self.case_name = case_name
        self.file_list = file_list
        self.file_uploader_list = [FileUploaderTask(self.client, self.case_name, os.path.abspath(file)) for file in
                                   self.file_list]
        all_task = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as pool:
            for file_uploader in self.file_uploader_list:
                all_task.append(pool.submit(file_uploader.run))
            print()
            print(f'{len(all_task)} uploading task is running')
            if daemon is False:
                print('daemon mode is True, wait until all tasks completed')
                while True:
                    self.print_status()
                    if all([task.done() for task in all_task]):
                        break
                    time.sleep(self.print_time_sleep)
                self.print_status()
            else:
                print('daemon mode is False, return immediately')
        if daemon is False:
            for uploader in self.file_uploader_list:
                if uploader.is_failed:
                    return False
            return True
        return

    def print_status(self):
        print()
        print(f"|{'id' : <6}|{'file' : <60}|{'type' : <40}|{'status' : <10}|{'message'}|")
        for uploader in self.file_uploader_list:
            print(uploader)
        sys.stdout.flush()


class FileUploaderTask(object):
    allowed_files = ['parquet']

    def __init__(self, client, case_name, filename):
        self.client = client
        self.filename = filename
        self.case_name = case_name
        self.case_id = None
        self.client = client
        self.case_type = None
        self.table = None
        self.md5 = None
        self.upload_url = None

        self.message = ''
        self.upload_status = CaseStatusEnum.waiting

    @property
    def is_failed(self):
        if self.upload_status == CaseStatusEnum.failed:
            return True
        return False

    def run(self):
        try:
            if not self.check():
                return
            self.upload_status = CaseStatusEnum.uploading
            self.pre_upload()
            if self.is_failed:
                return
            self.upload()
            if self.is_failed:
                return
            self.post_upload()
            if self.is_failed:
                return
            self.upload_status = CaseStatusEnum.uploaded
            self.message = f"upload finished"
        except Exception as e:
            self.upload_status = CaseStatusEnum.failed
            self.message = repr(e)

    @retry(tries=3)
    def pre_upload(self):
        param = {
            'name': self.case_name,
            'type': self.case_type,
            'status': CaseStatusEnum.waiting.value,
            'file': self.md5
        }
        url = f'{self.client.root_url}/descriptor/'
        resp = self.client._post_with_token(url, param)
        if resp.status_code // 100 != 2:
            self.upload_status = CaseStatusEnum.failed
            self.message = f"pre upload failed"
            return
        r = resp.json()
        self.case_id = r.get("id")
        self.message = f"pre upload finished"

        url = f'{self.client.root_url}/descriptor/upload_url/{self.case_id}'
        resp = self.client.get_with_token(url)
        if resp.status_code // 100 != 2:
            self.upload_status = CaseStatusEnum.failed
            self.message = f"get upload url failed"
            return
        self.message = f"get upload url finished"
        r = resp.json()
        self.upload_url = r

    @retry(tries=5, delay=2, backoff=1.2, max_delay=5)
    def upload(self):
        object_name = self.upload_url.get('result').get('fields').get('key')
        data = self.upload_url.get('result').get('fields')
        http_url = self.upload_url.get('result').get('url')
        with open(self.filename, 'rb') as fd:
            files = {'file': (object_name, fd)}
            resp = requests.post(http_url, data=data, files=files)
        if resp.status_code // 100 != 2:
            self.upload_status = CaseStatusEnum.failed
            self.message = f"upload failed"
            raise Exception("上传失败: 正在重试")

    def post_upload(self):
        param = {"status": CaseStatusEnum.uploaded.value}
        url = f'{self.client.root_url}/descriptor/{self.case_id}'
        resp = self.client.put_with_token(url, param)
        if resp.status_code // 100 != 2:
            self.upload_status = CaseStatusEnum.failed
            self.message = f"update status failed"
            return

    def check(self):
        if not self.check_file():
            return False
        if not self.check_file_format():
            return False
        if not self.check_file_columns():
            return False
        with open(self.filename, 'rb') as fp:
            self.md5 = hashlib.md5(fp.read()).hexdigest()
        return True

    def check_file(self):
        if not os.path.isfile(self.filename):
            self.upload_status = CaseStatusEnum.failed
            self.message = f"{self.filename} not a file"
            return False
        return True

    def check_file_format(self):
        if os.path.basename(self.filename).endswith('parquet'):
            self.table = pd.read_parquet(self.filename)
        elif os.path.basename(self.filename).endswith('csv'):
            self.table = pd.read_csv(self.filename)
        else:
            self.upload_status = CaseStatusEnum.failed
            self.message = f"{self.filename} not have a parquet or csv suffix"
            return False
        return True

    def check_file_columns(self):
        case_types = dict()
        for name in dir(CheckCaseType):
            value = getattr(CheckCaseType, name)
            if not name.startswith('__') and not callable(value) and not name.startswith('_'):
                case_types[name] = value

        file_columns = [c.lower() for c in self.table.columns]
        for case, columns in case_types.items():
            for need_column in columns:
                if need_column not in file_columns:
                    break
            else:
                self.case_type = case
                break
        else:
            # 如果找不到则为is_valid
            self.upload_status = CaseStatusEnum.failed
            self.message = f'{self.filename} columns not valid'
            return False
        return True

    def __str__(self):
        return f"|{str(self.case_id): <6}|{str(os.path.basename(self.filename)) : <60}|{str(self.case_type) : <40}|{str(self.upload_status.value) : <10}|{self.message}|"
