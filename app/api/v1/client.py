from app.libs.redprint import Redprint
from flask import request
from app.validators.forms import ClientTypeEnum,ClientForm,UserEmailForm
from app.models.user import User
api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 表单 通常用于网页中
    # json 客户端中
    # 注册 登录
    # 参数 校验 接受参数
    # wtforms 验证表单
    print('hahahha')
    data = request.json
    print(data)
    form = UserEmailForm()
    print(form)
    if form.validate():
        # print('1232131')
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        promise[form.type.data]()
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data)
