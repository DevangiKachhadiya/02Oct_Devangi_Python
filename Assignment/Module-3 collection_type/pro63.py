# Write a Python program to returns sum of all divisors of a number.

def sum(n):
    tot = 0
    for i in range(1,n+1):
        if n % i == 0:
            tot += i
    return tot

n = int(input("Enter any number: "))
print("Sum of Divisor: ",sum(n))