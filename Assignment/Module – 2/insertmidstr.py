# Write a Python function to insert a string in the middle of a string.

def insert_string_middle(str, word):
    return str[:2] + word + str[2:]

print(insert_string_middle('[[]]', 'Hello Python'))


'''    
s1 = input("Enter a String1 :")
s2 = input("Enter a String2 :")
insert_middle_str = input("Enter middle str :")
new_str= f"{s1} {insert_middle_str} {s2}"
print(new_str)
'''