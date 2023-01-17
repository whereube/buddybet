from flask import Flask
from user import User
import uuid
from bet import Bet

def create_user():
    grandma = Bet.create(description='jag vill betta med dig')
    for person in Bet.select():
        print(person.description)

create_user()