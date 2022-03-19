# coding: utf-8
# 代替原本的ErrorCode功能，web服务和后期可能的微服务通用


class APICode(object):
    """
    Web和rpc接口返回的code
    """
    SUCCESS = 1
    ERROR = 3
    NOT_FOUND = 4
    # 预付充值多笔资金调用时，分别进行多笔的错误返回，定义特殊的code用于前端区分
    PREPAY_CHARGE_FAIL = 5
    # 服务器内部错误, 500错误
    SYSTEM_INNER_ERROR = -1
    # 请求参数不合法
    PARAMS_INVALID = 10
    # 没有可用的数据
    NO_AVAILABLE_DATA = 2
    # 权限不足
    PERMISSION_DENIED = 30
    # 调用接口失败
    CALL_INTERFACE_FAIL = 40
    # 非法的业务操作
    INVALID_OPERATION = 50
    # 获取锁超时
    LOCK_BLOCK_TIMEOUT = 60
    # 给前端code，不自动隐藏
    DATA_ERROR_NOT_HIDE = 70
    # 第三方token错误
    TOKEN_ERROR = 201
