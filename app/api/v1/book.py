from flask import Blueprint
from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/get')
def get_user():
    return 'get book'


@api.route('/create')
def create_book():
    return 'create book'
