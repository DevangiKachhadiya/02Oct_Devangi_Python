'''open("record.txt","w")
print("file is created")'''

f1=open("record.txt","a")

data=int(input("Enter number of student: "))

for i in range(data):
    id=input("Enter any id: ")
    name=input("Enter any name: ")
    city=input("Enter any city: ")

    f1.write(f"Id:{id}\nName:{name}\nCity:{city}\n")
    f1.write("======================================\n")

