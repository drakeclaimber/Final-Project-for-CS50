# Здесь будет основная работа с приложением, где будут выполняться методы POST и GET
import os
from helper import login_required
from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Создаём переменную, через которую будем работать с серверной частью сайта
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# TODO Сделать Dashboard
@app.route('/dashboard')
@login_required
def index():
    return render_template('dashboard.html')

# TODO Сделать Форму для регистрации 
@app.route('/register')
def register():
    return render_template("/register.html")

@app.route('/login')
def login():
    return render_template('/login.html')

