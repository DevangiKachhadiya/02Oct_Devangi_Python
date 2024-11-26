# Write a Python program to add 'ing' at the end of a given string (length
#should be at least 3). If the given string already ends with 'ing' then add
#'ly' instead if the string length of the given string is less than 3, leave it unchanged.

my_str=input("Enter string: ") 

print(len(my_str))
if len(my_str)>2:
    if my_str[-3:]=='ing':
        my_str += 'ly'
        print(my_str)
    else:
        my_str += 'ing'
        print(my_str)
else:
    print(my_str)

