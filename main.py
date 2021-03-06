import flask
from flask_login import LoginManager, login_user, login_required, logout_user
from flask import Flask,render_template, redirect
from data import db_session
from data.users import User
from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class RegFrom(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeat_password = PasswordField('Повторите пароль', validators=[DataRequired()])
    username = StringField('Имя пользователя', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')
    
   
class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    # remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/registration', methods=['GET', 'POST'])
def reg():
    form = RegFrom()
    if form.validate_on_submit():
        db_session.global_init("db/blogs.db")
        db_sess = db_session.create_session()
        user = User()
        if form.password.data == form.repeat_password.data:
            user.email = form.email.data
            user.password = form.password.data
            user.name = form.username.data
            db_sess.add(user)
            db_sess.commit()
            return redirect('/')
        return render_template('register.html',
                               message="пароли не совпадают",
                               form=form)
    return render_template('register.html', title='Зарегистрироваться', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_session.global_init("db/blogs.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
