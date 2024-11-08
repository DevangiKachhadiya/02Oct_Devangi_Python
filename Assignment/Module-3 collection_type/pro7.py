# Write a Python program to remove duplicates from a list.

list = [23,10,16,19,23,27,10,27]
print(list)
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
print(list2)
