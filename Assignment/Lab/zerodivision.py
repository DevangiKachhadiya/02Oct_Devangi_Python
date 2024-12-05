#Write a Python program to handle exceptions in a simple calculator 
#(division by zero, invalid input).
def calculator():
    try:
        n1=int(input("Enter number1: "))
        n2=int(input("Enter number2: "))
        operations=input("Enter operations(+,-,*,/): ")

        if operations=='+':
            result=n1+n2
        elif operations=='-':
            result=n1-n2
        elif operations=='*':
            result=n1*n2
        elif operations=='/':
            result=n1/n2
            if n2==0:
                print("can not divide by Zero")
        else:
            print("Invalid input")
        print(f"Result is: {result}")

    except :
        print("Error: Division by Zero")

calculator()