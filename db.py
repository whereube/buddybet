import mysql.connector as mysql
from peewee import *



mysql_db = MySQLDatabase('u522633204_buddy_bet', user='u522633204_buddy_bet', password='Buddy_bet2023',
                         host='sql927.main-hosting.eu')
mysql_db.connect()

# # enter your server IP address/domain name
# HOST = "sql927.main-hosting.eu" # or "domain.com"
# # database name, if you want just to connect to MySQL server, leave it empty
# DATABASE = "u522633204_buddy_bet"
# # this is the user you create
# USER = "u522633204_buddy_bet"
# # user password
# PASSWORD = "Buddy_bet2023"
# # connect to MySQL server
# db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
# print("Connected to:", db_connection.get_server_info())
# # enter your code here!

# cursor = db_connection.cursor()

# query = ("SELECT * FROM profile")

# cursor.execute(query)
# #
# for (name) in cursor:
#     for x in name:
#         print(x)

# cursor.close()
# db_connection.close()

