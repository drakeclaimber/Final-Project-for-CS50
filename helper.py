# Здесь будут прописаны доп функции для app.py
import requests

from flask import redirect, render_template, session
from functools import wraps

# Функция для проверки регистрации
def login_required(f):
  @wraps(f)
  def decarated_function(*args, **kwargs):
    if session.get("user_id") is None:
      return redirect('/login')
    return f(*args, **kwargs)
  
  return decarated_function