'''Write a Python function that takes a list and returns a new list with unique
elements of the first list'''
# using set and list with function
my_list=[1,2,3,4,5,6,4,2,1,3]
print(my_list)
my_set= set(my_list)
new_list=list(my_set)
print(new_list)
