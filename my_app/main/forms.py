from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('请输入用户名', validators=[DataRequired()])
    password = PasswordField('请输入密码', validators=[DataRequired()])
    remember_me = BooleanField('记住密码', default=False)
    submit = SubmitField('提交')
