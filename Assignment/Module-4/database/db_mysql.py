import pymysql

try:
    db=pymysql.connect(host="localhost",user="root",password='',database='mydb')
    print("\nDatabase is Connected")
except Exception as e:
    print(e)

cr=db.cursor()
#Table Create
tbl_create="create table stud(id integer primary key auto_increment,name varchar(20),city varchar(20),subject varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

#Insert Data