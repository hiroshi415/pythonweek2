import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='mydatabse'
)

mycursor = mydb.cursor()
sql = 'INSERT INTO student (name, address) VALUES (%s, %s)'
val = [('DOG', 'BANGALORE'),
       ('PUPPY', 'BANGALORE'),
       ('KITTY', 'BANGALORE'),
       ('CAT', 'BANGALORE')]

mycursor.executemany(sql, val)

mydb.commit()
