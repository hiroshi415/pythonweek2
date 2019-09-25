import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='spiceup'
)

# initialize cursor
mycursor = mydb.cursor()


# # sqlformula
# sqlFormula = "INSERT INTO teachers (name, gender, class) VALUES (%s, %s, %s)"
# students = [
#     ('Padma', 'female', 'IT'),
#     ('Rohit', 'male', 'IT'),
#     ('Rekha', 'female', 'IT'),
#     ('Pratima', 'female', 'English'),
#     ('Hiro', 'male', 'Intern'),
#     ]

# # execute SQL statement
# mycursor.executemany(sqlFormula, students)

# # this will actually change the data
# mydb.commit()

# mycursor.execute('SELECT * FROM students')
# # # will return all rows
# # myresult = mycursor.fetchall()

# # only return first row
# myresult = mycursor.fetchone()

# for row in myresult:
#     print(row)

'''
# WHERE keyword
# # if retrieving integer, single quote is ok
# sql = 'SELECT * FROM students WHERE age= 22'
# when retrieving string, start and close with double quote
#  and sandwich string with single quote
sql = "SELECT * FROM students WHERE class = 'English'"
'''

'''
# # WHERE a LIKE keyword
# sql = "SELECT * FROM students WHERE name = %s"

# mycursor.execute(sql, ('Hiroshi', ))

# myresult = mycursor.fetchall()

# for result in myresult: 
#     print(result)
# '''

# sql = "UPDATE students SET age = 32 WHERE name = 'Tokiya'"
# mycursor.execute(sql)

# # if you only need to see couple of data
# mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()

# for result in myresult:
#     print(result)

'''
# Ordering data
sql = "SELECT * FROM students ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for r in myresult:
    print(r)
'''

# Deleting
sql = "DELETE FROM students WHERE age = 20"
mycursor.execute(sql)

mydb.commit()