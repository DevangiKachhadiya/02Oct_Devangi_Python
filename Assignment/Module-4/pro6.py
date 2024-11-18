# WAP to read a file line by line and store it into a list.
list=[]
fl=open("demo1.txt","r")
#print(fl.readline().split())
for i in fl:
    if i not in list:
        list.append(i)
print(list)
   


