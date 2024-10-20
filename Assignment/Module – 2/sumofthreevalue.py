#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

x=int(input("Enter a number X: "))
y=int(input("Enter a number Y: "))
z=int(input("Enter a number Z: "))
sum = 0

if x==y or y==z or z==x :
    print("Sum is : ",0)
else:
    sum = x+y+z
    print("Sum is : ",sum)



 
