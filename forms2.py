from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, StringField, PasswordField, DateField
from wtforms.validators import InputRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Имя', validators=[InputRequired()])
    password = PasswordField('Пароль', validators=[InputRequired()])
    email = StringField('Почта', validators=[InputRequired(), Email()])
    datetime = DateField('Дата', format='%d/%m/%y', validators=[InputRequired()])
    remember_me = BooleanField('Запомнить меня', validators=[InputRequired()])
    i_agree = BooleanField('Я согласен с...', validators=[InputRequired()])
    submit = SubmitField('Субмит')
