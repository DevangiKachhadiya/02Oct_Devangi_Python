
n= int(input("enter no of elements pair : "))
my_dict = {}

for i in range(n):
    key=input("Enter your key: ")
    values=input("Enter your values: ")
    my_dict[key]=values

print(my_dict)
 
'''
n= int(input("enter no of elements pair : "))
my_dict = {}

for i in range(n):
    key=input("Enter your key: ")
    values=input("Enter your values: ")
    #my_dict['id']=key
    #my_dict['values']=values
    #print(f"{key} : {values}")
    for i in my_dict:
        print(i)
    for j in my_dict.values():
        print(j)
    for i,j in my_dict.items():
    #print(i,j)
        print(f"Key={i} and Value={j}")

print(my_dict)
'''
