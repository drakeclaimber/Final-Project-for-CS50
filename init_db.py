import sqlite3

connection = sqlite3.connect('transactions.db')

with connection:
  connection.execute('''
    CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hashed_password TEXT NOT NULL,
    total_expenses REAL NOT NULL,
    total_income REAL NOT NULL,
    total_balance REAL NOT NULL);
  ''')

  connection.execute('''
  CREATE TABLE IF NOT EXISTS expenses(
  user_id INTEGER NOT NULL,
  amount REAL NOT NULL,
  category TEXT NOT NULL,
  date TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id)
                     );
  ''')

  connection.execute('''
  CREATE TABLE IF NOT EXISTS income(
  user_id INTEGER NOT NULL,
  amount REAL NOT NULL,
  source TEXT NOT NULL,
  date TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id)
                     );
  ''')

