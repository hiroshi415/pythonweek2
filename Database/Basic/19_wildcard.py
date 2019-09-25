import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'customer'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee WHERE name LIKE '%oh%'")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)