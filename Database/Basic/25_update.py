import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'customer'
)

mycursor = mydb.cursor()

mycursor.execute('UPDATE employee SET salary = 9000 WHERE salary = 1000')

mydb.commit()