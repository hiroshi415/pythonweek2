import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='ecom'
)

mycursor = mydb.cursor()
mycursor.execute('ALTER TABLE category ADD COLUMN category_product VARCHAR(25)')
sql = "INSERT INTO category (category_name, category_product) "
val = [
    ('JOHN', 'JOHNNY'),
    ('JOHN', 'JOHNNY'),
    ('JOHN', 'JOHNNY'),
    ('JOHN', 'JOHNNY'),
]

mycursor.executemany(sql, val)

mydb.commit()
