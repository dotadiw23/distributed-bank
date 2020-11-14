from flask import Flask, jsonify, request
from central.api import db_manager as db
import jwt

app = Flask(__name__)


# Test
@app.route('/ping/<string:token>')
def pong(token):

    try:
        decoded = jwt.decode(token, 'secret', algorithm='HS256')
        return jsonify(decoded)
    except:
        return jsonify('Invalid Token')


# Gives to the user a token if the sent credentials are valid
@app.route('/login', methods=['POST'])
def get_account():
    try:
        account_no = request.json['account_no']
        password = request.json['password']
        access = db.search_client(account_no, password)

        if len(access) > 0:
            return jsonify(jwt.encode({"_id" : access[0]}, 'secret', algorithm='HS256'))

        return jsonify("Account not found")
    except:
        return jsonify("Invalid request")


if __name__ == '__main__':
    app.run(host='192.168.0.3', debug=True)
