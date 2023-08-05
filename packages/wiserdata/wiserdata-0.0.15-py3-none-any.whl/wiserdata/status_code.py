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
    code = 400
    msg = "param 参数错误, 返回码: %(code)s; 返回信息: %(result)s"


class LoginException(APIException):
    code = 401 | 403
    msg = "登陆失败, 返回码: %(code)s; 返回信息: %(result)s"


class ServerException(APIException):
    code = 500
    msg = "服务器端内部错误, 返回码: %(code)s; 返回信息: %(result)s"


class OtherException(APIException):
    code = "other"
    msg = "未知异常: 返回码: %(code)s; 返回信息: %(result)s"


class StatusCode:

    ERROR_CODE_DICT = {
        400: ParamException,
        401: LoginException,
        413: LoginException,
        500: ServerException,
    }
    CURRENT_CODE_LIST = [200, 201, 203, 204, 205, 206]

    def __init__(self, resp: Response):
        self.r = resp
        self.code = self.r.status_code

    def check_login_status_code(self):
        if self.code == 200:
            result = self.r.json()
            _access_token = result['access_token']
            return _access_token

        result = self.ERROR_CODE_DICT.get(self.code, None)
        if issubclass(result, APIException):
            err_message = self.r.json().get('message')
            raise result(code=self.code, result=err_message)
        else:
            err_message = self.r.json().get('message')
            raise OtherException(code=self.code, result=err_message)

    def check_post_status_code(self):
        if self.code in self.CURRENT_CODE_LIST:
            return self.r

        result = self.ERROR_CODE_DICT.get(self.code, None)
        if issubclass(result, APIException):
            err_message = self.r.json().get('message')
            raise result(code=self.code, result=err_message)
        else:
            err_message = self.r.json().get('message')
            raise OtherException(code=self.code, result=err_message)
