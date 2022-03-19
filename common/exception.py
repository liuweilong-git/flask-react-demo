# coding: utf-8
from common.api_code import APICode


class APIException(Exception):
    def __init__(self, api_code, msg=''):
        Exception.__init__(self, msg)
        self.api_code = api_code


class EndException(APIException):
    """
    终止异常，不再重复处理, 用于mq消费，功能重试等场景下明确无需进行失败重试
    """
    def __init__(self, status_code, msg=u''):
        """

        :param status_code:
        :param msg:
        """
        APIException.__init__(self, status_code, msg)


class RuntimeException(Exception):
    """
    运行时异常
    """
    def __init__(self, msg, runtime_exception=None):
        """
        :param runtime_exception:
        """
        Exception.__init__(self, msg)
        self.runtime_exception = runtime_exception
# 用于各种条件检测，如果检测失败，抛出APIException, 默认code为参数非法
# def check(boolean, error_msg, status_code=APICode.PARAMS_INVALID, api_exception=True):
#     if not boolean:
#         raise (APIException(status_code, error_msg) if api_exception else Exception(error_msg))


def check(boolean, error_msg, status_code=APICode.PARAMS_INVALID, api_exception=True):
    try:
        if not boolean:
            raise (APIException(status_code, error_msg) if api_exception else Exception(error_msg))
    except APIException:
        return status_code, error_msg
    except Exception:
        return status_code, error_msg
