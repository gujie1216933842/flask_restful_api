from app.libs.redprint import Redprint

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 表单 通常用于网页中
    # json 客户端中
    # 注册 登录
    # 参数 校验 接受参数
    # wtforms 验证表单
    pass
