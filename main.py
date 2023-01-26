from flask import Flask
from user import User
import uuid
from bet import Bet
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=['GET'])
def create_user():
    result = []
    for bet in Bet.select():
        result.append(bet.description)
    return result

if __name__ == '__main__':
    app.run()