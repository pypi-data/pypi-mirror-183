import copy
import json
import threading
import prison
import requests
import pandas as pd

from datetime import datetime

from .config import Config
from .checker import Checker, class_lists
from .checker import clickhouse_to_pandas


class BaseClient(object):
    _threading_local = threading.local()

    def __init__(self):
        self._instance = None

    @classmethod
    def instance(cls):
        _instance = getattr(cls._threading_local, '_instance', None)
        if _instance is None:
            _instance = cls()
            cls._threading_local._instance = _instance
        return _instance


class BaseRemoteClient(BaseClient):
    _threading_local = threading.local()

    def __init__(self):
        super().__init__()
        self.host = Config.host
        self.port = Config.port
        self._refresh_token = None
        self._access_token = None
        self._instance = None
        self.root_url = f'http://{self.host}:{self.port}/api/v1'

    def get_with_token(self, url):
        if self._access_token is None:
            raise Exception("Login required")
        headers = {
            "Authorization": f'Bearer {self._access_token}'
        }
        r = requests.get(url, headers=headers)
        return r

    def put_with_token(self, url, param):
        if self._access_token is None:
            raise Exception("Login required")
        headers = {
            "Authorization": f'Bearer {self._access_token}'
        }
        r = requests.put(url, json=param, headers=headers, timeout=5*60)
        return r

    def _post_with_token(self, url, param):
        headers = {
            "Authorization": f'Bearer {self._access_token}'
        }
        r = requests.post(url, json=param, headers=headers)
        return r

    def _login(self, username, password, refresh=True):
        url = f'{self.root_url}/security/login'
        if refresh:
            body = {
                "username": username,
                "password": password,
                "provider": 'db',
                "refresh": True
            }
        else:
            body = {
                "username": username,
                "password": password,
                "provider": 'db'
            }
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.post(url, data=json.dumps(body), headers=headers)
        return r

    def _refresh(self, refresh_token):
        url = f"{self.root_url}/security/refresh"
        headers = {
            "Authorization": f'Bearer {refresh_token}'
        }
        r = requests.post(url, headers=headers)
        return r

    def login(self, username, password):
        try:
            r = self._login(username, password, refresh=False)
            result = r.json()
            if r.status_code == 200:
                # login succeed
                self._access_token = result['access_token']
            else:
                if result.get('message', None) is not None:
                    raise Exception(f"登陆失败, 返回码: {r.status_code}, 返回值:{result.get('message', None)}")
                raise Exception(f"登陆失败, 返回码: {r.status_code}, 返回值:{result}")
        except Exception as e:
            raise Exception(f"Login 请求出现错误: {e}")

    def post_with_token(self, url, param):
        if self._access_token is None:
            raise Exception("Login required")
        try:
            r = self._post_with_token(url, param)

            try:
                result = r.json()
            except Exception:
                raise Exception(f"连接断开 {r.text}")

            if r.status_code in [200, 201]:
                return r
            else:
                error_message = result.get('message', None)
                if error_message is None:
                    raise Exception(f"请求失败, 返回码: {r.status_code}, 返回值:{result}")
                raise Exception(f"请求失败, 返回码: {r.status_code}, 返回值:{error_message}")
        except Exception as e:
            raise Exception(f"Post 请求失败: {e}")


class RemoteClient(BaseRemoteClient):

    def __init__(self):
        super().__init__()

    def _response_to_dataframe(self, resp: requests.Response) -> pd.DataFrame:
        if resp.headers["Content-Type"] == "application/json; charset=utf-8":
            result = resp.json()
            df = pd.DataFrame.from_records(result['data'])
        elif resp.headers["Content-Type"] == "text/tsv; charset=utf-8":
            content = json.loads(resp.text)
            data = content["data"]
            columns = [i["name"] for i in content["meta"]]
            df = pd.DataFrame(data, columns=columns)
            dtype = {
                decription['name']: self._filter_data(decription['type'])
                for decription in content["meta"]
            }

            copy_dtype = copy.deepcopy(dtype)

            for key in copy_dtype:
                null_count = df[key].isnull().sum()
                if 'int' in dtype[key] and null_count > 0:
                    dtype[key] = 'float64'

            df = df.astype(dtype)

        else:
            df = pd.DataFrame()
        return df

    def _response_to_characteristic(self, resp: requests.Response) -> pd.DataFrame:
        if resp.headers["Content-Type"] == "text/tsv; charset=utf-8":
            content = json.loads(resp.text)
            data = content["data"]
            columns = [i["name"] for i in content["meta"]]
            df = pd.DataFrame(data, columns=columns)
            if 'code' in columns:
                df['code'].astype('object')
        else:
            df = pd.DataFrame()
        return df

    def _filter_data(self, data):
        filter_nullable = data.replace('Nullable(', '').replace(')', '')

        if "Decimal" in filter_nullable:
            return clickhouse_to_pandas['Decimal']

        data_type = clickhouse_to_pandas.get(filter_nullable, "object")
        return data_type

    def query_sheet(self, param) -> pd.DataFrame:
        q = {k: v for k, v in param.items() if k not in ["domain", "phylum", "class"]}
        url = f'{self.root_url}/{param.get("domain")}/{param.get("phylum")}/{param.get("class")}'
        resp = self.post_with_token(url, q)
        df = self._response_to_dataframe(resp)
        return df

    def query_descriptor(self, param) -> pd.DataFrame:
        url = f'{self.root_url}/{param.get("domain")}/{param.get("phylum")}/{param.get("class")}'
        resp = self.post_with_token(url, param)
        if param.get('phylum') == 'characteristic':
            df = self._response_to_characteristic(resp)
            return df
        df = self._response_to_dataframe(resp)
        return df

    def query(self, param) -> pd.DataFrame:
        if param["domain"] == "sheet":
            if param['phylum'] in ['ths', 'jn']:
                res = self.ths_or_jn_sheet(param)
            else:
                res = self.query_sheet(param)
        elif param["domain"] == "descriptor":
            res = self.query_descriptor(param)
        else:
            raise Exception("Params error, invalid domain")
        return res

    def extract_sheet(self, param) -> pd.DataFrame:
        if param["class"].find('ths') >= 0:
            param["phylum"] = "direct"
        url = f'{self.root_url}/{param.get("domain")}/{param.get("phylum")}/extract'
        q = param
        resp = self.post_with_token(url, q)
        df = self._response_to_dataframe(resp)
        return df

    def ths_or_jn_sheet(self, param) -> pd.DataFrame:
        url = f'{self.root_url}/sheet/{param["phylum"]}/{param["phylum"]}'
        q = param
        resp = self.post_with_token(url, q)
        df = self._response_to_dataframe(resp)
        return df

    def extract_descriptor(self, param) -> pd.DataFrame:
        url = f'{self.root_url}/{param.get("domain")}/{param.get("phylum")}/extract'
        q = param
        resp = self.post_with_token(url, q)
        if param["class"].find("synthesis") > 0:
            return resp.json()['data']
        else:
            df = pd.DataFrame.from_records(resp.json()['data'])
            return df

    def extract_feature_synthesis(self, param):
        url = f'{self.root_url}/{param.get("domain")}/{param.get("phylum")}/feature_synthesis'
        q = param
        resp = self.post_with_token(url, q)
        res = dict()
        for k, v in resp.json()["data"].items():
            res[k] = pd.DataFrame.from_records(v)
        return res

    def extract(self, param):
        if param["domain"] == "sheet":
            res = self.extract_sheet(param)
        elif param["domain"] == "descriptor":
            res = self.extract_descriptor(param)
        else:
            raise Exception("Params error, invalid domain")
        return res

    def query_upload_status(self, trade_date):
        trade_date = trade_date.get("trade_date")
        try:
            trade_date = datetime.strptime(trade_date, '%Y%m%d').strftime('%Y-%m-%d')
        except Exception as e:
            raise Exception(f"{trade_date} format error, valid format '%Y%m%d'")
        url = f'{self.root_url}/warehouse/status/'
        if self._access_token is None:
            raise Exception("Login required")
        headers = {
            "Authorization": f'Bearer {self._access_token}'
        }
        params = {
            "filters": [
                {
                    "col": "date",
                    "opr": "eq",
                    "value": trade_date
                }
            ]
        }
        q = prison.dumps(params)
        r = requests.get(url, params={"q": q}, headers=headers)
        if r.status_code != 200:
            message = r.json().get("message")
            raise Exception(f"Query Status failed, error message{message}")
        else:
            return r.json()

    def is_ready_to_upload(self, trade_date):
        r = self.query_upload_status(trade_date)
        if r.get("result"):
            return True if r.get("result")[0].get("is_data_ready") == 1 else False
        return False

    def notify_upload_finished(self, trade_date):
        trade_date = trade_date.get("trade_date")
        try:
            trade_date = datetime.strptime(trade_date, '%Y%m%d').strftime('%Y-%m-%d')
        except Exception as e:
            raise Exception(f"{trade_date} format error, valid format '%Y%m%d'")
        url = f'{self.root_url}/warehouse/status/'
        if self._access_token is None:
            raise Exception("Login required")
        headers = {
            "Authorization": f'Bearer {self._access_token}'
        }
        params = {
            "date": trade_date,
            "is_data_uploaded": 1
        }
        r = requests.post(url, json=params, headers=headers)
        if r.status_code not in [200, 201]:
            raise Exception(f"notify failed, error message: {r.json().get('message')}")


