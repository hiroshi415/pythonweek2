import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'customer'
)

mycursor = mydb.cursor()

# by default it is ascending order
mycursor.execute("SELECT * FROM employee ORDER BY salary DESC")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)