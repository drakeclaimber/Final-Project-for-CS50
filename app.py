# Здесь будет основная работа с приложением, где будут выполняться методы POST и GET
import os
from helper import login_required
from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Создаём переменную, через которую будем работать с серверной частью сайта
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if __name__ == '__main__':
    app.run(debug=True)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# TODO Сделать Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# TODO Сделать Форму для регистрации 
@app.route('/register')
def register():
    return render_template("register.html")

# TODO Сделать Форму для login
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    #Очистить сессию
    session.clear()
    #Вернуться на Log in
    redirect('/login')

# TODO Сделать Форму для индекс
@app.route('/')
@login_required
def index():
    return render_template('index.html')