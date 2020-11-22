import sqlite3
from sqlite3 import Error
from datetime import datetime


def connect():
    try:
        conn = sqlite3.connect('./central/database/bank.db')
        return conn
    except Error:
        print(Error.__annotations__)


def search_client(account_no, password):
    conn = connect()
    cursor = conn.cursor()
    params = (account_no, password,)
    cursor.execute('SELECT account_no FROM accounts WHERE account_no = ? AND password = ?', params)

    rows = cursor.fetchall()
    account_no = []

    for row in rows:
        account_no.append(row[0])

    if conn:
        conn.close()

    return account_no


def get_account(account_no):
    conn = connect()
    cursor = conn.cursor()
    params = (account_no,)
    cursor.execute('SELECT * FROM accounts WHERE account_no = ?', params)

    rows = cursor.fetchall()
    user = []

    for row in rows:
        user.append(row[0])
        user.append(row[1])
        user.append(row[2])
        user.append(row[4])

    if conn:
        conn.close()

    return user


def get_transactions(account_no):
    conn = connect()
    cursor = conn.cursor()
    params = (account_no, account_no)
    cursor.execute('SELECT * FROM transactions WHERE origin = ? OR destination = ?', params)

    rows = cursor.fetchall()
    transactions = []

    for row in rows:
        transactions.append({
            'transaction_id': row[0],
            'origin': row[1],
            'destination': row[2],
            'amount': row[3],
            'transaction_date': row[4]
        })

    if conn:
        conn.close()

    return transactions


def make_transaction(account_no, destination, amount):
    conn = connect()
    cursor = conn.cursor()
    transaction_date = datetime.now().strftime("%Y-%m-%d")

    try:
        params1 = (account_no, destination, amount, transaction_date,)
        params2 = ((get_amount(account_no)-amount), account_no, )
        params3 = ((get_amount(destination) + amount), destination)

        cursor.execute('INSERT INTO transactions (origin, destination, amount, transaction_date) VALUES (?, ?, ?, ?)',
                       params1)
        cursor.execute('UPDATE accounts SET amount = ? WHERE account_no = ?', params2)
        cursor.execute('UPDATE accounts SET amount = ? WHERE account_no = ?', params3)

        conn.commit()

        if conn:
            conn.close()

        return 1
    except Error:
        print(Error)
        return 0


def get_amount(account_no):
    conn = connect()
    cursor = conn.cursor()
    params = (account_no,)
    cursor.execute("SELECT amount FROM accounts WHERE account_no = ?", params)

    rows = cursor.fetchall()
    amount = 0

    for row in rows:
        amount = row[0]

    if conn:
        conn.close()

    return float(amount)


def exists(destination):
    conn = connect()
    cursor = conn.cursor()
    params = (destination,)
    cursor.execute("SELECT account_no FROM accounts WHERE account_no = ?", params)

    rows = cursor.fetchall()

    for row in rows:
        return len(row[0]) > 0

    if conn:
        conn.close()
