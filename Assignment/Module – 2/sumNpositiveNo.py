# Write a python program to sum of the first n positive integers

n = int(input("Enter positive integer : "))
sum = 0
for i in range(n+1):
    sum += i
print(sum)

