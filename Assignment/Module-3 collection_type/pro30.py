# Write a Python program to convert a list of tuples into a dictionary.
user_list=[]
list=int(input("Enter your number of elements: "))

for i in range(list):
    key = input("Enter your keys: ")
    value = input("Enter your values: ")
    user_list.append((key,value))

x=dict(user_list)
print(x)