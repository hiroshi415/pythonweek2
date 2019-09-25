import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'customer'
)

mycursor = mydb.cursor()

mycursor.execute('DELETE FROM employee WHERE salary=900')

mydb.commit()
