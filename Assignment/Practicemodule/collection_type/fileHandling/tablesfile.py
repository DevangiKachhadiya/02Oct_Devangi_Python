'''open("readtables.txt","x")
print("File is created")
'''
f1=open("tables.txt","w")
n1= int(input("Enter No of tables:"))

for i in range(n1):
    n=int(input("Enter No: "))
    for j in range(1,11):
        print(f"{n}*{j}={n*j}\n")
        f1.write(f"{n}*{j}={n*j}\n")
    f1.write("===================\n")



