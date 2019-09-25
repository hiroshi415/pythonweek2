import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'mydatabse'
)

mycursor = mydb.cursor()
mycursor.execute('ALTER TABLE student ADD COLUMN contact INT(25)')