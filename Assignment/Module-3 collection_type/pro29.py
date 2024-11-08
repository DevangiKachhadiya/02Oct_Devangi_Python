# Write a Python program to unzip a list of tuples into individual lists.
tuple_list=[(1,'h',10.7),(2,'n',19.3),(3,'b',27.6)]
print(list(zip(*tuple_list)))
