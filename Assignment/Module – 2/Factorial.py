# Write a Python program to get the Factorial number of given number.

number = int(input("Enter a number: "))
Factorial = 1
if number < 0 :
    print("Factorial does not exist for negative numbers ")
elif number == 0 :
    print("Factorial of 0 is 1")
else :
    for i in range(1,number + 1):
        Factorial = Factorial * i
    print("Factorial of",number,"is",Factorial)

