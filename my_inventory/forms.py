from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    submit_button = SubmitField()


class LegoForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    price = DecimalField('price', places=2)
    difficulty = StringField('difficulty')
    piece_count = IntegerField('piece_count')
    lego_category = StringField('lego_category')
    submit_button = SubmitField()