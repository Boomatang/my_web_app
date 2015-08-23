from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, RadioField, IntegerField, \
    DateField

__author__ = 'boomatang'
__version__ = '1'

class create_user(Form):

    first_name = StringField([validators.input_required(), validators.length(min=3, max=50)])
    surname = StringField([validators.input_required(), validators.length(min=3, max=50)])
    email = StringField([validators.input_required(), validators.length(min=5, max=50)])
    password = PasswordField([validators.input_required(), validators.length(min=6, max=50)])
    re_password = PasswordField([validators.input_required(), validators.length(min=6, max=50)])

    user_level = IntegerField()
    join_date = IntegerField()

