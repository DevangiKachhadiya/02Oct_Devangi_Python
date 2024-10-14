# WAP that will return true if the two given integer values are equal or their sum or difference is 5.

def check_nums(a,b):
    if a==b or abs(a-b) == 5 or (a+b) == 5 :
        return True
    else :
        return False

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

result = check_nums(num1,num2)
print(result)
 