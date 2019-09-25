import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'mydatabse'
)

mycursor = mydb.cursor()

sql = "INSERT INTO newtable (name, contact) VALUES ('%s', %d)"
val = ('JOHN', 123456789)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'row has been inserted')