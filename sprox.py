from sprox.formbase import AddRecordForm
from formencode import Schema
from formencode.validators import FieldsMatch
from tw.forms import PasswordField, TextField

form_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))
class RegistrationForm(AddRecordForm):
    __model__ = User
    __require_fields__     = ['password', 'user_name', 'email_address']
    __omit_fields__        = ['_password']
    __field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password']
    __base_validator__     = form_validator
    email_address          = TextField
    display_name           = TextField
    verify_password        = PasswordField('verify_password')

registration_form = RegistrationForm(DBSession)
