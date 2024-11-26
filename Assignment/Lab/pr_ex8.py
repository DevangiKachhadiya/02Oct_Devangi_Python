#to handle multiple exceptions(e.g.,file not found,division by zero).
try:
    n1=int(input("Enter No1. : "))
    n2=int(input("Enter No2. : "))
    result=n1/n2
    print(result)

    try:
        open("FILE.txt","r")
        fl=open("FILE.txt","r")
        print(fl.read())
    
    except FileNotFoundError:
        print("File not Found")

except ZeroDivisionError:
    print("Zero Division Error")
