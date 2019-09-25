# deleting the table if the data exists

import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'customer'
)

mycursor = mydb.cursor()

# it will run without error even if the data is not there
mycursor.execute('DROP TABLE IF EXISTS for_deleting')

mydb.commit()