import pandas as pd
from retry import retry
from .uploader import CaseTypeEnum
from .uploader import Uploader
from .checker import Checker
from .client import RemoteClient
from .client_local import LocalClient

__all__ = ['login', 'query', 'extract', 'get_client', 'update', 'is_ready_to_upload', 'notify_upload_finished']


def get_client(mode: str = 'local'):
    if mode == 'remote':
        client = RemoteClient.instance()
    else:
        client = LocalClient.instance()
    return client


# 为了兼容，保留接口
@retry(tries=5, delay=2, backoff=1.2, max_delay=5)
def login(username, password):
    """通过username和password登陆，设置token"""
    client = RemoteClient.instance()
    client.login(username, password)


@retry(tries=5, delay=2, backoff=1.2, max_delay=5)
def query(param):
    """查询接口"""
    client = RemoteClient.instance()
    # todo
    Checker.check_params(param)
    d = client.query(param)
    return d


@retry(tries=5, delay=2, backoff=1.2, max_delay=5)
def extract(param):
    """提取接口"""
    client = RemoteClient.instance()
    Checker.check_params(param)
    d = client.extract(param)
    return d


@retry(tries=5, delay=2, backoff=1.2, max_delay=5)
def update(case_name: str, file_list: list, daemon=True):
    """上传数据接口"""
    client = RemoteClient.instance()
    uploader = Uploader(client)
    uploader.upload(case_name, file_list, daemon=daemon)


def query(param):
    """查询接口"""
    client = RemoteClient.instance()
    Checker.check_params(param)
    d = client.query(param)
    return d


def is_ready_to_upload(date):
    """查询接口"""
    client = RemoteClient.instance()
    d = client.is_ready_to_upload(date)
    return d


def notify_upload_finished(date):
    """查询接口"""
    client = RemoteClient.instance()
    d = client.notify_upload_finished(date)
    return d
