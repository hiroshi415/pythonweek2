import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='customer'
)

mycursor = mydb.cursor()

sql = ("SELECT * FROM employee WHERE address = %s")
adr = ('bangalore1', )

mycursor.execute(sql, adr)

myrresult = mycursor.fetchone()

for x in myrresult:
    print(x)
