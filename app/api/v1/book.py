from flask import Blueprint
from app.libs.redprint import Redprint


api = Redprint('book')
@api.route('')
def get_user():
    return 'i am qiyue'