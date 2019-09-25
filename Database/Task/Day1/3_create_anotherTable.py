import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='ecom'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE Category (id INT AUTO_INCREMENT PRIMARY KEY, category_name VARCHAR(25))')