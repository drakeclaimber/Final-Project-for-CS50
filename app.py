# Здесь будет основная работа с приложением, где будут выполняться методы POST и GET
from flask import Flask, request, render_template 

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')