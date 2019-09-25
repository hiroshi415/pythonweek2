import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='ecom'
)

mycursor = mydb.cursor()


mycursor.execute('CREATE TABLE User (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), contact INT(25), email VARCHAR(25))')