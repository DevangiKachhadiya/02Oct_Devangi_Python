# Write a Python program to get unique values from a list.

list=['apple','mango','cherry','mango','guavava','apple']
list1=[ ]
for i in list: 
    if i not in list1:
        list1.append(i)
print(list1)  

