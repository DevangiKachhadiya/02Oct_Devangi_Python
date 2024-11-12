f1=open("demo.txt","w")

id=input("Enter any Id: ")
Name=input("Enter any Name: ")
city=input("Enter any City: ")

print(f"ID :",id)
print(f"Name:",Name)
print(f"City:",city)

f1.write(f"Id:{id},Name:{Name},City:{city}")
