from wtforms import Form, RadioField, StringField, PasswordField, validators, IntegerField, TextAreaField

__author__ = 'boomatang'
__version__ = '1'


class Create_User(Form):
    first_name = StringField([validators.input_required(), validators.length(min=3, max=50)])
    surname = StringField([validators.input_required(), validators.length(min=3, max=50)])
    email = StringField([validators.input_required(), validators.length(min=5, max=50)])
    password = PasswordField([validators.input_required(), validators.length(min=6, max=50)])
    re_password = PasswordField([validators.input_required(), validators.length(min=6, max=50)])

    user_level = IntegerField()
    join_date = IntegerField()


class UserLogin(Form):
    email = StringField([validators.input_required(), validators.length(min=5, max=50)])
    password = PasswordField([validators.input_required(), validators.length(min=6, max=50)])


class Comment(Form):
    comment_body = TextAreaField([validators.input_required(), validators.length(min=4, max=1000)])
    comment_rating = RadioField("Your Rating", choices=(("1", 'hi'),("2", "jbhup9"), ("3", "There now")))