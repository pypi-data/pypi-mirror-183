
from requests import Response

from .exception import ParamException, LoginException, ServerException, APIException, OtherException


class CheckStatus:

    CURRENT_CODE_LIST = [200, 201, 203, 204, 205, 206]

    QUERY_ERROR_CODE_DICT = {
        400: ParamException,
        401: LoginException,
        413: LoginException,
        500: ServerException,
    }

    def __init__(self, resp: Response):
        self.r = resp
        self.code = self.r.status_code

    def check_login_status_code(self):
        if self.code == 200:
            result = self.r.json()
            _access_token = result['access_token']
            return _access_token
        self._public_check()

    def check_post_status_code(self):
        if self.code in self.CURRENT_CODE_LIST:
            return self.r
        if self.code == 404:
            raise ParamException(code=self.code, result="phylum 参数可能错误")

        self._public_check()

    def _public_check(self):
        result = self.QUERY_ERROR_CODE_DICT.get(self.code, None)
        err_message = self.r.json().get('message')
        if issubclass(result, APIException):
            raise result(code=self.code, result=err_message)
        else:
            raise OtherException(code=self.code, result=err_message)
