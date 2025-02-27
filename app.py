# Здесь будет основная работа с приложением, где будут выполняться методы POST и GET
import os
from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')