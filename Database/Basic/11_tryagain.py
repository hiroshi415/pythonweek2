import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'mydatabse'
)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE student(name VARCHAR(25), address VARCHAR(25))')

sql = 'INSERT INTO student (name, address) VALUES (%s, %s)'
val = ('JOHN', 'BANGALORE12')

mycursor.execute(sql, val)

mydb.commit()