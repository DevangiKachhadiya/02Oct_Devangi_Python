import sqlite3

try:
    db=sqlite3.connect("newdb.db") #Create/connect a database
    print("DataBase Connected!") 
except Exception as e:
    print(e)

#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"

try:
    db.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)

# Insert Data
'''Insert_data="insert into studinfo(name,city)values('a','Ahmadabad'),('b','Baroda'),('c','Rajkot'),('d','Jamnagar'),('f','Surat')"
try:
    db.execute(Insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)'''

# Update Data
Update_data="update studinfo set name='Gannu' where name='Ganesh'"
try:
    db.execute(Update_data)
    db.commit()
    print("Record Updated")
except Exception as e:
    print(e)

# Delete Data
Delete_data="delete from studinfo where id=25"
try:
    db.execute(Delete_data)
    db.commit()
    print("Record Deleted")
except Exception as e:
    print(e)

# Show Data
cr=db.cursor()
Show_data="select *from studinfo"
try:
    cr.execute(Show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    
    for i in data:
       print(i)

    for i in data:
        print(i[1])

except Exception as e:
    print(e)


