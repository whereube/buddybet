from peewee import *

mysql_db = MySQLDatabase('u522633204_buddy_bet', user='u522633204_buddy_bet', password='Buddy_bet2023',
                         host='sql927.main-hosting.eu')
                         
class Profile:
    name = CharField()
    birthday = DateField()

    class Meta:
        database = mysql_db # This model uses the "people.db" database.