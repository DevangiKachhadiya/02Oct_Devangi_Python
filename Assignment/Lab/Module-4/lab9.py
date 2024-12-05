'''Write a Python program to connect to an SQLite3 database, 
create a table, insert data, and fetch data.'''

import sqlite3
try:
    db=sqlite3.connect("database.db")
    print("Database is Connected")
except Exception as e:
    print(e)

# Table Create
tbl_create="create table Tops(id integer primary key autoincrement,name text,city rajkot,subject text)"
try:
    db.execute(tbl_create)
    print("Table Created")
except Exception as e:
    print(e)

'''# Insert Data
insert_data="insert into Tops(name,city,subject) values ('shiv','rajkot','python'),('shakti','jamnagar','python'),('ram','surat','designing')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)'''

# Fetch Data
cr=db.cursor()
fetch_data="select *from Tops"
try:
    cr.execute(fetch_data)
    data=cr.fetchall()
    print("Record Fetched!")

    for i in data:
        print(i)
        
except Exception as e:
    print(e)