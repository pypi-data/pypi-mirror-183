from requests import Response


class APIException(Exception):
    msg = "Something unknown went wrong"
    code = 500

    def __init__(self, **kwargs):
        if 'msg' in kwargs:
            msg = kwargs.get("msg")
        else:
            msg = self.msg
        self.msg = msg % kwargs
        Exception.__init__(self, self.msg)


class ParamException(APIException):
    # code = 400 | 404
    msg = "param 参数错误, 返回码: %(code)s; 返回信息: %(result)s"


class LoginException(APIException):
    # code = 401 | 403
    msg = "登陆失败, 返回码: %(code)s; 返回信息: %(result)s"


class ServerException(APIException):
    # code = 500
    msg = "服务器端内部错误, 返回码: %(code)s; 返回信息: %(result)s"


class OtherException(APIException):
    code = "other"
    msg = "未知异常: 返回码: %(code)s; 返回信息: %(result)s"


