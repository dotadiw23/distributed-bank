from flask import Flask, jsonify, request
from central.api import db_manager as db
import jwt
import os
from dotenv import load_dotenv

app = Flask(__name__)


# Test
@app.route('/ping/<string:token>')
def pong(token):
    try:
        decoded = jwt.decode(token, os.getenv('TOKEN_SECRET'), algorithm='HS256')
        return jsonify(decoded)
    except:
        return jsonify('Invalid Token')


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


@app.route('/account/<string:user_token>', methods=['GET'])
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



if __name__ == '__main__':
    load_dotenv()
    app.run(host=os.getenv('API_HOST'), debug=True)
