from flask import Blueprint
from app.libs.redprint import Redprint


api = Redprint('user')
@api.route('', methods=['GET'])
def get_user():
    print('hahahahhahahhahaha')
    return 'get user'