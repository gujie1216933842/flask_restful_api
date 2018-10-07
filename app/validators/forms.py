from app.libs.enums import ClientTypeEnum
from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, length


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired])

    def validate_type(self):
        pass
