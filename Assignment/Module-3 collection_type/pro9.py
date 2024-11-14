# Write a Python function that takes two lists and returns true if they have at least one common member.
def Number(list1,list2):
    com_num = False

    for i in list1:
        if i in list2:
            com_num = True
    return com_num

list1 = [1,2,3,4]
list2 = [3,7,9,6]

ans=Number(list1,list2)
print(ans)


