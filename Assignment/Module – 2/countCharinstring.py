# Write a Python program to count the number of characters (character frequency) in a string

str = "HELLO WORLD"
print(str)

dict = {}
for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)