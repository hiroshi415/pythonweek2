import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'mydatabse'
)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE newTable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25))')