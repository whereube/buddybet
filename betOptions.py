from peewee import *
from bet import Bet
from user import User

mysql_db = MySQLDatabase('u522633204_buddy_bet', user='u522633204_buddy_bet', password='Buddy_bet2023',
                         host='sql927.main-hosting.eu')

class BetOptions(Model):
    bet_id = ForeignKeyField(Bet, backref='bets')
    user_id = ForeignKeyField(User, backref='users')
    option = CharField(max_length=100)

    class Meta:
        database = mysql_db 


