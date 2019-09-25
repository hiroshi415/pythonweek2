import sqlite3
import time
import datetime
import random


conn = sqlite3.connect('HW.db')
c = conn.cursor()


def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS category(name VARCHAR(255), slug VARCHAR(255))")
    c.execute("CREATE TABLE IF NOT EXISTS product_list(name VARCHAR(255), slug VARCHAR(255), price INT(255), stock INT(255), created_date VARCHAR(255))")


def product_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(
        unix).strftime('%Y-%m-%d %H:%M'))

    stock = (random.randrange(5,20))    
    price = (random.randrange(10, 50))
    c.execute("INSERT INTO product_list (price, stock, created_date) VALUES (?, ?, ?)",
              (price, stock, date)
              )
    conn.commit()

def category_data_entry():
    name = 'jewellery'
    slug = 'jewellery-acc'
    c.execute("INSERT INTO category (name, slug) VALUES (?, ?)",
              (name, slug)
              )
    conn.commit()

def show_data():
    c.execute('SELECT * FROM category')
    for row in c.fetchall():
        print(row)

def clean_product_data():
    c.execute("DELETE FROM product_list WHERE name IS NULL")
    conn.commit()
def clean_category_data():
    c.execute("DELETE FROM category WHERE name IS NULL")
    conn.commit()

# create_table()
# for i in range(9):
#     product_data_entry()
# category_data_entry()

# name = [('earring'),('jeans'),('mobile'),('necklace'),('php'),('pillow'),('sofa'),('top'),('washing-machine')]
# slug = [('earring'),('jeans'),('mobile'),('necklace'),('php'),('pillow'),('sofa'),('top'),('washing-machine')]
# c.execute('SELECT * FROM product_list')
# for row in c.fetchall():
#     for i in range(0, len(name)):
#         c.execute("UPDATE product_list SET name = (?), slug = (?) WHERE ROWID = (?) ", (name[i], slug[i], i))
#         conn.commit()

# clean_product_data()
# clean_category_data()
show_data()
c.close()
conn.close()