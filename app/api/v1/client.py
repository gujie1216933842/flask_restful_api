from app.libs.redprint import Redprint
from flask import request
from app.validators.forms import ClientTypeEnum,ClientForm,UserEmailForm
from app.models.user import User
from werkzeug.exceptions import HTTPException
from app.libs.error_code import Success
api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 表单 通常用于网页中
    # json 客户端中
    # 注册 登录
    # 参数 校验 接受参数
    # wtforms 验证表单
    data = request.json
    print('aaaaaaaaaaa')
    form = ClientForm().validate_for_api()
    print('bbbbbbbbbbb')
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
