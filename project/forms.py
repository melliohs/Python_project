from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from data.users import User


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=20, message="Должно быть от 2 до 20 символов") ])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(min=2, max=20, message="Должно быть от 2 до 20 символов")])
    username = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20, message="Должно быть от 2 до 20 символов")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8, max=25, message="Должно быть от 8 до 25 символов")])
    confirm_password = PasswordField('Подтвердить', validators=[DataRequired(),
                                                        EqualTo('password', message="Пароли не совпадают")])
    submit = SubmitField('Зарегистрироваться')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class UpdateAccountForm(FlaskForm):
    name = StringField('Имя',
                       validators=[DataRequired(), Length(min=2, max=20, message="Должно быть от 2 до 20 символов")])
    surname = StringField('Фамилия',
                          validators=[DataRequired(), Length(min=2, max=20, message="Должно быть от 2 до 20 символов")])
    username = StringField('Логин',
                           validators=[DataRequired(), Length(min=2, max=20, message="Должно быть от 2 до 20 символов")])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Фотография профиля', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Обновить')



class AddNewsForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    author = StringField('Автор', validators=[DataRequired()])
    date = StringField('Дата', validators=[DataRequired()])
    category = StringField('Категория', validators=[DataRequired()])
    image = FileField('Изображение', validators=[FileAllowed(['jpg', 'png'])])
    description = TextAreaField('Описание', validators=[DataRequired()])
    small_description = TextAreaField('Короткое описание', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class AddGuidesForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    author = StringField('Автор', validators=[DataRequired()])
    date = StringField('Дата', validators=[DataRequired()])
    image = FileField('Изображение', validators=[FileAllowed(['jpg', 'png'])])
    description = TextAreaField('Описание', validators=[DataRequired()])
    small_description = TextAreaField('Короткое описание', validators=[DataRequired()])
    submit = SubmitField('Добавить')