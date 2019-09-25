import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'mydatabse'
)

mycursor = mydb.cursor()

# mycursor.execute('ALTER TABLE newtable ADD COLUMN email VARCHAR(25)')
mycursor.execute('ALTER TABLE newtable ADD COLUMN contact INT(25)')