# wiserdata的使用方法

## 安装wiserdata
```shell
pip install wiserdata
```

## 本地调用
本地调用需要通过同步工具将数据文件保存在本地后再调用接口进行数据查询


执行命令
```python
import wiserdata as wi
client = wi.LocalClient(path="XXX/XXX/XXX")    # path为数据文件的保存根目录
param = {
    'domain': 'descriptor',
    'phylum': 'feature',
    'class': 'aindexeodprices',
    'fields': [],
    'user': '0000001',
    'case': 'equity_20220628',
    'start_date': '20220628',
    'end_date': '20220630',
    'codes': [],
    'form': 'normal'
}
client.query(param)
```

## 远程调用
执行命令
### query
```python
import wiserdata as wi
wi.login(username='XXX', password='XXX')
param = {
    'domain': 'descriptor',
    'phylum': 'feature',
    'class': 'aindexeodprices',
    'fields': [],
    'user': '0000001',
    'case': 'equity_20220628',
    'start_date': '20220628',
    'end_date': '20220630',
    'codes': [],
    'form': 'normal'
}
wi.query(param)
```

### extract
```python
import wiserdata as wi
wi.login(username='XXX', password='XXX')
param = {
    'domain': 'descriptor',
    'phylum': 'feature',
    'class': 'aindexeodprices',
    'fields': [],
    'user': '0000001',
    'case': 'equity_20220628',
    'start_date': '20220628',
    'end_date': '20220630',
    'codes': [],
    'form': 'normal'
}
wi.query(param)
```

### update

```python
import pandas as pd
import wiserdata as wi

wi.login(username='XXX', password='XXX')
case_name = "测试数据"
case_type = "characteristic_exposure"
df = {'characteristic': ['fac001', 'fac002'], 'exposure': [3, 4], 'date': ['2021-08-03', '2021-08-03'],
       'type': ['equity', 'equity'], 'code': ['stk01', 'stk02'] }
tbl = pd.DataFrame(data=df)

# 上传数据
wi.update(case_name, case_type, tbl)

# 上传成功后通过query查询上传的数据
param = {
    'case': '测试数据',
    'user': '',   
    'domain': 'descriptor',
    'phylum': 'characteristic',
    'class': 'characteristic_exposure',
    'fields': [],
    'start_date': '20210803',
    'end_date': '20210803',
    'codes': [],
}
res = wi.query(param)
print(res)

```

