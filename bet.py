from peewee import *

mysql_db = MySQLDatabase('u522633204_buddy_bet', user='u522633204_buddy_bet', password='Buddy_bet2023',
                         host='sql927.main-hosting.eu')

class Bet(Model):
    description = CharField(max_length=500)
    stake = IntegerField()

    class Meta:
        database = mysql_db 

