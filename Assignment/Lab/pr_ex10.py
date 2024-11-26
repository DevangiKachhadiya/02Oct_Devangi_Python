# Write a Python program to print custom exceptions.

try:
    n1=int(input("Enter number1: "))
    n2=int(input("Enter number2: "))
    result=n1/n2
    print(result)

except ValueError:
    print("Error: Invalid input,please enter numeric values.")

except:
    print("Zero division Error")

