import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'customer'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM employee LIMIT 4')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)