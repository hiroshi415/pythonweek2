# you can write condition

import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'customer'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee WHERE address = 'bangalore1'")

myresult = mycursor.fetchone()

for x in myresult:
    print(x)