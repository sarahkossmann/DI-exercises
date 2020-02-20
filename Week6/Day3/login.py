import flask_wtf
import wtforms
from wtforms import validators

class Form(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username", [validators.Length(min=4, max=25)])
    password = wtforms.PasswordField("Password", [validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")