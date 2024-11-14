#Write a Python function to get the largest number, smallest num and sum of all from a list.
list=[23,19,27,16,10,66,99,37]
print("original list:",list)
list.sort()
print("sorted list:",list)

def getlist(sum,smallest,largest):
    print("sum of all is :",sum)
    print("smallest number is :",smallest)
    print("largest number is :",largest)
   
smallest=(list[0])
largest=(list[-1])
sum=0
for i in list:
    sum+=i

getlist(sum,smallest,largest)
