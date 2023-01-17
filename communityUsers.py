from peewee import *
from user import User
from community import Community

mysql_db = MySQLDatabase('u522633204_buddy_bet', user='u522633204_buddy_bet', password='Buddy_bet2023',
                         host='sql927.main-hosting.eu')

class CommunityUsers(Model):
    user_id = ForeignKeyField(User, backref='users')
    community_id = ForeignKeyField(Community, backref='communities')

    class Meta:
        database = mysql_db 
