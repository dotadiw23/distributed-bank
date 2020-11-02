import sqlite3
from sqlite3 import Error
from central.account import Account
from datetime import datetime


def connect():
    try:
        conn = sqlite3.connect('./database/bank.db')
        return conn
    except Error:
        print(Error)


def get_accounts():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts')

    rows = cursor.fetchall()
    accounts = {}

    for row in rows:
        accounts[str(row[0])] = Account(row[0], row[1], row[2], '', row[3])

    if conn:
        conn.close()

    return accounts


def get_offices():
    return ['']


def search_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    params = (username, password,)
    cursor.execute('SELECT * FROM employees WHERE username = ? AND password = ?', params)

    rows = cursor.fetchall()
    user = []

    for row in rows:
        user.append(row[1])
        user.append(row[2])
        user.append(row[3])
        user.append(row[4])

    if conn:
        conn.close()

    return user


def create_account(account, amount, owner):
    conn = connect()
    cursor = conn.cursor()
    created_at = datetime.now()
    params = (account, amount, owner, created_at)
    try:
        cursor.execute('INSERT INTO accounts (account_no, mount, owner, created_at) VALUES (?, ?, ?, ?)', params)
        conn.commit()

        if conn:
            conn.close()

        return created_at
    except Error:
        print(Error)
        return ''


def delete_account(account):
    conn = connect()
    cursor = conn.cursor()
    params = (account,)

    try:
        cursor.execute('DELETE FROM accounts WHERE account_no = ?', params)
        conn.commit()

        if conn:
            conn.close()

        return True
    except Error:
        return False
