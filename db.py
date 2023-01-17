from peewee import *
from user import User
from community import Community
from communityUsers import CommunityUsers
from bet import Bet
from betOptions import BetOptions

mysql_db = MySQLDatabase('u522633204_buddy_bet', user='u522633204_buddy_bet', password='Buddy_bet2023',
                         host='sql927.main-hosting.eu')
mysql_db.connect()
mysql_db.create_tables([User])
mysql_db.create_tables([Community])
mysql_db.create_tables([CommunityUsers])
mysql_db.create_tables([Bet])
mysql_db.create_tables([BetOptions])


# grandma = User.create(name='Kalle')
# for person in User.select():
#     print(person.name)




