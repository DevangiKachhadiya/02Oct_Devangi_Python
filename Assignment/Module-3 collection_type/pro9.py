# Write a Python function that takes two lists and returns true if they have at least one common member.
def Number(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False

list1 = [1,2,3,4]
list2 = [3,7,9,6]

answer = Number(list1,list2)
print(answer)