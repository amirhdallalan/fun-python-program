#database name = user_info
#table name = login

import mysql.connector
import re

email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

cnx = mysql.connector.connect(user = 'root', password = 'Ee8GvLZpdh', host = 'localhost',
                             database = 'user_info')
cursor = cnx.cursor()
check = False
while (not check):
    email = input()
    password = input()

    if(re.fullmatch(email_format, email)):
        cursor.execute("INSERT INTO login VALUES (%s,%s);", (email, password))
        check = True
    else:
        print("Please insert valid email: expression@string.string")
    cnx.commit()
