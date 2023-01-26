from flask import Flask, request
from user import User
import uuid
from bet import Bet
from flask_cors import CORS
from db import create_user_in_bd

app = Flask(__name__)
CORS(app)


@app.route("/create_user", methods=['POST'])
def create_user():
    print("till databasen")
    name = request.headers.get("name")
    password = request.headers.get("password")
    email = request.headers.get("email")
    print(name)
    create_user_in_bd(name, password, email)
    return "User created"
    


if __name__ == '__main__':
    app.run()