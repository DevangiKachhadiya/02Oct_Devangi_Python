#Write a Python program to replace last value of tuples in a list.
tuples=[(10,27,3),(16,19,6),(23,17,9)]
new_value= 76

x= [i[:-1] + (new_value,) for i in tuples]
print(x)
