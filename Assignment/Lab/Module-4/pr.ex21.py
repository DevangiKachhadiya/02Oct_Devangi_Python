'''Write a Python program to create a database and a table using
SQLite3. '''

# Create Database
import sqlite3
try:
    db=sqlite3.connect("mydb.db")
    print("Database Created")
except Exception as e:
    print(e)

# Create Table

tbl_create="create table mytbl(id integer primary key autoincrement,name text,age integer)"
try:
    db.execute(tbl_create)
    print("Table Created")
except Exception as e:
    print(e)