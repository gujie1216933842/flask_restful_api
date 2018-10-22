'''项目的入口文件'''
from app import create_app

app = create_app()
# print('hahahahha')
#
# @app.route('/v1/user/get')
# def get_user():
#     return 'i am gujie'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9000)
