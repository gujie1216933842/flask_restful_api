from flask import request

from wtforms import Form
from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        print(data)
        args = request.args.to_dict()
        print(args)
        '''super(BaseForm,self) 首先找到 BaseForm 的父类（就是类 Form），然后把类B的对象 BaseForm 转换为类 Form 的对象'''
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        print('ccccccccc')
        valid = super(BaseForm, self).validate()
        # print(valid)
        print('ddddddddd')
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
