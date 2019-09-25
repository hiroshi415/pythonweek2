import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'customer'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM employee')

# # fetching all
# myresult = mycursor.fetchall()

# # fetching one
# myresult = mycursor.fetchone()

# specify item numbers
myresult = mycursor.fetchmany(8)

for x in myresult:
    print(x)