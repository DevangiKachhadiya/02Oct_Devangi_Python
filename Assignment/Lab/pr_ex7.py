# Write a Python program to handle exceptions in a calculator.
def calculator():
    try:
        n1=int(input("Enter number1: "))
        n2=int(input("Enter number2: "))
        operations=input("Enter Operations(+,-,*,/) : ")

        if operations=='+':
            result=n1+n2

        elif operations=='-':
            result=n1-n2
    
        elif operations=='*':
            result=n1*n2

        elif operations=='/':
            result=n1/n2

        else:
            print("Invalid input")
        print(f"Result is: {result}")

    except Exception as e:
        print("Error:",e)

    finally:
        print("Calculation is done")

calculator()