# Write a Python program to demonstrate handling multiple exceptions.
try:
    n1=int(input("Enter a number1: "))
    n2=int(input("Enter number2: "))
    result=n1/n2
    print("Division is : ",result)

except ValueError:
    print("Error: Invalid input,please enter numeric values.")

except ZeroDivisionError:
    print("Error:Zero Division Error")

except Exception as e:
    print("Unexpected Error:",e)

finally:
    print("Multiple exceptions done")
