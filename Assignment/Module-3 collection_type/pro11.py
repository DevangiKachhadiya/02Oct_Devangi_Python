'''Write a Python function that takes a list and returns a new list with unique
elements of the first list'''

def get_unique(my_list):
    unique_ele = [ ]
    for i in my_list:
        if i not in unique_ele:
            unique_ele.append(i)
    return unique_ele

my_list=[1,2,3,4,5,6,4,2,1,3]
print(get_unique(my_list))

