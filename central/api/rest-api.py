from flask import Flask, jsonify, request
from central.api import db_manager as db
import jwt
import os
from dotenv import load_dotenv
from central.api import pyro_manager

app = Flask(__name__)


# Test
@app.route('/ping')
def pong():
    pyro_manager.update_account_state("1234", "8888")
    return jsonify('pong')


# Gives to the user a token if the sent credentials are valid
@app.route('/login', methods=['POST'])
def login():
    try:
        account_no = request.json['account_no']
        password = request.json['password']
        access = db.search_client(account_no, password)

        if len(access) > 0:
            return jsonify(jwt.encode({"_id": access[0]}, os.getenv('TOKEN_SECRET'), algorithm='HS256'))

        return jsonify("Account not found")
    except Exception:
        return jsonify("Invalid request")


# Return the bank account information
@app.route('/account/<string:user_token>')
def get_account(user_token):
    try:
        decoded_token = jwt.decode(user_token, os.getenv('TOKEN_SECRET'), algorithms='HS256')
    except:
        return jsonify('Invalid Token')

    account_info = db.get_account(decoded_token['_id'])
    return jsonify({
        'account_no': account_info[0],
        'amount': account_info[1],
        'owner': account_info[2],
        'created_at': account_info[3]
    })


# Return a list of the users transactions
@app.route('/transactions/<string:user_token>')
def get_transactions(user_token):
    try:
        decoded_token = jwt.decode(user_token, os.getenv('TOKEN_SECRET'), algorithms='HS256')
    except:
        return jsonify('Invalid Token')

    transactions_list = db.get_transactions(decoded_token['_id'])

    return jsonify(transactions_list)


# make_transaction returns:
# 5 -> If the account does not have enough money
# 4 -> The destination account does not exists
# 3 -> If a database error has occurred
# 2 -> If the request is not valid
# 1 -> If the transaction is successful
# 0 -> The transaction has failed
@app.route('/transactions/<string:user_token>', methods=['POST'])
def make_transactions(user_token):
    try:
        decoded_token = jwt.decode(user_token, os.getenv('TOKEN_SECRET'), algorithms='HS256')
    except:
        return jsonify('Invalid Token')

    try:
        destination = request.json['destination']
        if destination == decoded_token['_id']:
            return jsonify(2)

        amount = request.json['amount']
        try:
            account_amount = db.get_amount(decoded_token['_id'])
            destination_exists = db.exists(destination)

            if account_amount > amount:
                if destination_exists:
                    transaction_status = db.make_transaction(decoded_token['_id'], destination, amount)

                    pyro_manager.update_account_state(decoded_token['_id'], destination)

                    return jsonify(transaction_status)
                else:
                    return jsonify(4)
            else:
                return jsonify(5)
        except:
            return jsonify(3)
    except:
        return jsonify(2)


if __name__ == '__main__':
    load_dotenv()
    app.run(host=os.getenv('API_HOST'), debug=True)
