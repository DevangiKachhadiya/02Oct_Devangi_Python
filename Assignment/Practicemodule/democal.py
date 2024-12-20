n1 = int(input("Enter Number1: "))
n2 = int(input("Enter Number2: "))
Op=input("Enter Operation (+,-,*,/): ")

if Op == '+' :
    result = n1 + n2
    print(f"Result is: {result}")

elif Op == '-' :
    result = n1 - n2
    print(f"Result is: {result}")

elif Op == '*' :
    result = n1 * n2
    print(f"Result is: {result}")

elif Op == '/' :
    result = n1 / n2
    print(f"Result is: {result}")

else:
    print("Wrong input!")

