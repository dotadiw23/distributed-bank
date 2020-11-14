import sqlite3
from sqlite3 import Error


def connect():
    try:
        conn = sqlite3.connect('../database/bank.db')
        return conn
    except Error:
        print(Error.__annotations__)


def search_client(account_no, password):
    conn = connect()
    cursor = conn.cursor()
    params = (account_no, password,)
    cursor.execute('SELECT account_no FROM accounts WHERE account_no = ? AND password = ?', params)

    rows = cursor.fetchall()
    user = []

    for row in rows:
        user.append(row[0])

    if conn:
        conn.close()

    return user

