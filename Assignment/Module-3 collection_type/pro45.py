# Write a Python program to find the highest 3 values in a dictionary.
dict={'a':100,'b':27,'c':39,'d':40,'h':50,'n':600}
list=[]
for i in dict.values():
    list.append(i)
list.sort()
print("highest value:",list[-1])
print("second highest value:",list[-2])
print("third highest value:",list[-3])
