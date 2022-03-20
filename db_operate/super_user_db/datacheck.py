from models import SuperUserModel
from werkzeug.security import generate_password_hash, check_password_hash


class UserService(object):

    @staticmethod
    def check_password(data):
        # my_set_username = "123"  # 真实账号
        # my_set_password = "123"  # 真实账号
        my_set_password_md5 = generate_password_hash("123")  # 真实密码的md5
        # print(my_set_password_md5) # 由于没有注册管理员的地方，所以选择直接获得加密的密码，直接查库，然后去查询（不会写前端hah)
        user = SuperUserModel.query.filter_by(username=data.get("username")).first()
        if user:
            try:
                if data["username"] == user.username and check_password_hash(user.password, data["password"]):
                    # 验证成功
                    re = {'code': 0, 'message': "验证通过"}
                else:
                    re = {'code': 1, 'message': "验证失败"}
            except Exception as e:
                print(repr(e))
                re = {'code': -1, 'message': repr(e)}
            return re
        else:
            re = {'code': -1, 'message': "用户不存在"}
            return re
