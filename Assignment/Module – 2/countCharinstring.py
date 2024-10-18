# Write a Python program to count the number of characters (character frequency) in a string

string = "HELLO WORLD"
print(string)

for i in string:
    char = string.count(i)
    print(str(i) + ": " + str(char), end=", ")
