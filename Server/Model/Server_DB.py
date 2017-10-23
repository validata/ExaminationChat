### ALPHA PREVIEW ###

import sqlite3
from sqlite3 import Error

sqlite_path = 'Users.db'
table_name = 'Table'
f1 = 'ID'
f2 = 'Username'
f3 = 'Nickname'
f4 = 'Password'
field_type = 'INTEGER'

# Connecting
conn_sql = sqlite3.connect(sqlite_path)
c = conn_sql.cursor()

id_counter = 0

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS UserData(unix REAL, username TEXT, password TEXT, nickname TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO UserData VALUES(12414114,'MyUserName', 'MyPassword', 'MyNickname', 5)")
    conn_sql.commit()
    c.close()
    conn_sql.close()

def read_from_db():

    c.execute('SELECT * FROM UserData')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)

# create_table()
# data_entry()
read_from_db()

c.close()
conn_sql.close()