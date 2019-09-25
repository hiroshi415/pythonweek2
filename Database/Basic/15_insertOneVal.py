import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'mydatabse'
)

mycursor = mydb.cursor()

sql = "INSERT INTO demo (name) VALUES ('JOHN')"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'row has been inserted')