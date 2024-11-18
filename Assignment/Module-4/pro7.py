#  WAP to read a file line by line store it into a variable.
data=" "
fl=open("data.txt","r")
print(fl.readline())
'''for i in fl:
    if i not in data:
        print(data)
'''