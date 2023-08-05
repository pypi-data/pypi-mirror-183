import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

params_name_lists = ['domain', 'phylum', 'class', 'fields', 'start_date', 'end_date', 'codes', 'case', 'user', 'form']
domain_lists = ['sheet', 'descriptor']
phylum_lists = ['trading', 'direct', 'characteristic', 'feature', 'bond', 'financial', 'consensus']
class_lists = ['asharecalendar', 'ashareeodprices', 'ashareeodderivativeindicator', 'asharettmhis',
               'aindexeodprices', 'ashareswindustriesclass', 'asharefinancialindicator', 'asharebalancesheet',
               'ashareincome', 'asharecashflow', 'asharedividend', 'ashareconsensusdata', 'asharestockratingconsus',
               'ashareconsensusrollingdata',
               'cbondcurvecnbd', 'extract', 'characteristic_exposure',
               'characteristic_return', 'characteristic_covariance', 'characteristic_idiosyncratic_volatility',
               'feature_exposure', 'feature_return', 'feature_covariance', 'feature_idiosyncratic_volatility']
clickhouse_to_pandas = {
    "UInt8": "int64",
    "UInt16": "int64",
    "UInt32": "int64",
    "UInt64": "int64",
    "UInt128": "int64",
    "UInt256": "int64",
    "Int8": "int64",
    "Int16": "int64",
    "Int32": "int64",
    "Int64": "int64",
    "Int128": "int64",
    "Int256": "int64",

    "Float32": "float64",
    "Float64": "float64",

    "String": "string",
    "Decimal": "float64",
    "DateTime": "datetime64[ns]"
}


class Checker(object):
    @classmethod
    def check_params(cls, client_params):
        """判断参数中是否存在异常字段"""
        for param_name in client_params.keys():
            if param_name not in params_name_lists:
                raise Exception(f"Param errors, {param_name} were unexpected")
                return False
        """判断 domain phylum class 在参数中是否存在以及值是否正确"""
        if "domain" not in client_params.keys():
            raise Exception(f"Param errors, param domain not exists")
        if client_params['domain'] not in domain_lists:
            raise Exception(f"Param errors, param domain value error")
        if "phylum" not in client_params.keys():
            raise Exception(f"Param errors, param phylum not exists")
        if client_params['phylum'] not in phylum_lists:
            raise Exception(f"Param errors, param phylum value error")
        if "class" not in client_params.keys():
            raise Exception(f"Param errors, param class not exists")
        if client_params['class'] not in class_lists:
            if client_params['phylum'] == 'direct':
                pass
            else:
                raise Exception(f"Param errors, param class value error")
        logger.info("Client param is ok")


if __name__ == '__main__':
    param = {
        'domain': 'sheet',
        'phylum': 'trading',
        'class': 'asharecalendar',
        'fields': ['TRADE_DAYS', 'S_INFO_EXCHMARKET'],
        'start_date': '20180101',
        'end_date': '20221231',
        'codes': ['000300.SH']
    }
    c = Checker()
    c.check_params(param)

