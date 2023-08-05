import datetime
import os
import glob

import pandas as pd
import pyarrow.parquet as pq

from .client import BaseClient

characteristic_list = ['characteristic_exposure', 'characteristic_return', 'characteristic_covariance',
                       'characteristic_idiosyncratic_variance', 'characteristic_scale']


class LocalClient(BaseClient):
    def __init__(self, path):
        super().__init__()
        if not os.path.isdir(path):
            raise Exception(f"{path} is not a valid directory")
        self.storage_path = path

    def query(self, param):
        if param.get("domain") == "descriptor" and param.get("phylum") == "characteristic":
            return self.query_descriptor(param)
        else:
            raise Exception("Parameter error, domain or phylum error")

    def query_descriptor(self, param):
        self._check_storage_path()
        self._check_query_descriptor(param)
        self._check_date(param.get("start_date"))
        self._check_date(param.get("end_date"))

        path = os.path.join(self.storage_path, f'{param.get("class")}*')
        parquet_files = glob.glob(path)
        print(f'loading {parquet_files} files')
        if not parquet_files:
            raise Exception(f"Parameter error, parquet files does not exist")
        filters = self._gen_query_filters(param)
        dataset = pq.ParquetDataset(parquet_files, use_legacy_dataset=False, filters=filters)
        df = dataset.read().to_pandas()
        df.sort_values(by=['date'])
        return df

    def _gen_query_filters(self, param):
        filters = [[]]
        if param.get("start_date") and param.get("start_date") != "":
            filters[0].append(('date', '>=', param.get('start_date')))
        if param.get("end_date") and param.get("end_date") != "":
            filters[0].append(('date', '<=', param.get('end_date')))
        if param.get("case"):
            filters[0].append(('case', '==', param.get('case')))
        return filters

    def _check_date(self, date: str):
        if date is None or date == "":
            return

    def _check_storage_path(self):
        if not os.path.isdir(self.storage_path):
            raise Exception(f"{self.storage_path}该目录不存在")

    def _check_query_descriptor(self, param):
        if param.get("class") not in characteristic_list:
            raise Exception("Parameter error, class error")
        if param.get("case") is None:
            raise Exception("Parameter error, case error")

    def extract(self, param):
        pass
