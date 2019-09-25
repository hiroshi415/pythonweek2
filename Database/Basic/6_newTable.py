import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'mydatabse',
)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE cust(name VARCHAR(25), address VARCHAR(25), id INT(10), contact INT(10))')