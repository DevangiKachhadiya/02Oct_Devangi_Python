# Write a Python function to check whether a number is perfect or not.
def is_perfect(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total == number

num = int(input("Enter a number: "))
if is_perfect(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")