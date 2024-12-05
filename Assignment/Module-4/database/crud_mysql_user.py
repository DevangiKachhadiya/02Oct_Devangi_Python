import pymysql

try:
    db=pymysql.connect(host="localhost",user="root",password='',database='newdb')
    print("\nDatabase is Connected")
except Exception as e:
    print(e)


print("\nChoose any option")
print("\t1.Create Table")
print("\t2.Record Insert")
print("\t3.Record Update")
print("\t4.Record Delete")
print("\t5.Read Data")
print("\t6.Exit")

n=int(input("\nEnter Any Number which you want to perform: "))

cr=db.cursor()
#Table Create
if n == 1 :
    tbl_create="create table studinfo(id integer primary key,name varchar(20),city varchar(20))"
    try:
        cr.execute(tbl_create)
        db.commit()
        print("Table Created")
    except Exception as e:
        print(e)

elif n == 2 :
    id=int(input("Enter ID: "))
    name=input("Enter Name: ")
    city=input("Enter City: ")
    
    
    try:
        Insert_data="insert into studinfo(id,name,city) values (%s, %s, %s)"
        cr.execute(Insert_data,(id, name, city))
        db.commit()
        print("Record Inserted!")
    except Exception as e:
        print(e)

elif n == 3 :
    user_id=int(input("Enter the user ID to update: "))
    new_name=input("Enter new name: ")
    new_city=input("Enter new city: ")
    
    try:
        Update_data="update studinfo set name= %s, city= %s where id= %s"
        cr.execute(Update_data, (new_name,new_city,user_id))
        db.commit()
        print("Record Updated")
    except Exception as e:
        print(e)

elif n == 4 :
    user_id=int(input("Enter user ID to delete: "))
    
    try:
        Delete_data="delete from studinfo where id= %s"
        cr.execute(Delete_data,(user_id,))
        db.commit()
        print("Record Deleted")
    except Exception as e:
        print(e)

elif n == 5 :
    
    try:
        Show_data="select *from studinfo"
        cr.execute(Show_data)
        data=cr.fetchall()
            
        for i in data:
            print(i)

    except Exception as e:
        print(e)

elif n == 6 :
    print("Exit the Application!")

else:
    print("Invalid input.Please choose a valid option.")


