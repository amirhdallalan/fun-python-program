#database name = karmandan
#table name = info
from os import close
from weakref import ProxyTypes
import mysql.connector

cnx = mysql.connector.connect(user = 'root', password = 'Ee8GvLZpdh', host = 'localhost',
                             database = 'karmandan')
cursor = cnx.cursor()

cursor.execute(""" SELECT * FROM info """)
data = cursor.fetchall ()
info = []
for row in data:
    info.append(row)

info.sort(key= lambda x: x[1])
info.sort(key= lambda x: -x[2])
for person in info:
    print (person[0],person[2],person[1])