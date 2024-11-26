# Write a Python program to get the Factorial number of given number.
n=int(input("enter a number: "))
fact=1
for i in range(2,n+1):
    fact=fact*i
print(f"Factorial of {n} is {fact}",end="")