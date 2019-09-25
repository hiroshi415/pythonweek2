import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'mydatabse',
)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE demo(name VARCHAR(25))')