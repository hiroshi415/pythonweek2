import sqlite3

dbase = sqlite3.connect('Our_data.db') #Open a database File
print('database opened')

dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL
)''')
print('table created')

def insert_record(ID,NAME,DIVISION, STARS):
    dbase.execute('''INSERT INTO employee_records (ID, NAME, DIVISION, STARS) 
    VALUES(?, ?, ?, ?)''',(ID, NAME, DIVISION,STARS))
    dbase.commit()
    print('Records inserted')

insert_record(5, 'BOBby', 'TEACHER', 2)

def read_Data():
    data = dbase.execute('''SELECT * FROM employee_records ORDER BY ID''')
    for record in data:
        print('ID: '+str(record[0]))
        print('NAME: '+str(record[1]))
        print('DIVISION: '+str(record[2]))
        print('STARS: '+str(record[3]))

def update_record():
    dbase.execute('''UPDATE employee_records SET STARS=5 WHERE ID=2''')
    dbase.commit()
    print('UPDATED')

def delete_record():
    dbase.execute('''DELETE FROM employee_records WHERE ID = 2''')
    dbase.commit()
    print('Deleted')


# update_record()
delete_record()
print('-------------------------------------')
read_Data()

dbase.close()
print('database closed')
