import re

name=input("Enter Name: ")
name_pattern="[A-Za-z]"
x=re.findall(name_pattern,name)
if x:
    print("Name is Valid")
else:
    print("Error.Invalid Name")
#===========================================================
    
Email=input("Enter an Email: ")
Email_pattern="^[a-z0-9_.]+[@]+[a-z]+[\.]+[a-z]{2,}$"
x=re.findall(Email_pattern,Email)
if x:
    print("Email is Valid")
else:
    print("Error.Invalid Email")
#============================================================
    
MobileNo=input("Enter a Mobile No. : ")
MobileNo_pattern="[0-9]"
y=MobileNo
if y.isdigit() and int(len(y)) == 10 :
    print("Mobile Number Is Valid ")
else:
    print("Error.Invalid input")
#=============================================================
    
Password=input("Enter a Password: ")
Password_pattern="[a-zA-Z0-9_.@]{4,}$"
z=re.findall(Password_pattern,Password)
if z:
    print("Password is valid")
else:
    print("Error.Invalid Password")

#================================================================
Confirm_PassWord=input("Enter a Confirm Password: ")
Confirm_PassWord_pattern="[a-zA-Z0-9_.@]{4,}$"
a=re.findall(Confirm_PassWord_pattern,Confirm_PassWord)
if a:
    print(" valid password")
    if Password==Confirm_PassWord:
        print("Password Matched")
    else:
        print("Password Not Match ")
else:
    print("Error. Invalid password")

#================================================================