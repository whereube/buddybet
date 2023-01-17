from peewee import *


mysql_db = MySQLDatabase('u522633204_buddy_bet', user='u522633204_buddy_bet', password='Buddy_bet2023',
                         host='sql927.main-hosting.eu')
                         
class User(Model):
    id = UUIDField(primary_key=True)
    name = CharField(max_length=50)
    password = CharField(max_length=50)
    email = CharField(max_length=50)
    
    class Meta:
        database = mysql_db 