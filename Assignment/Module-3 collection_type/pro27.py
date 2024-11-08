# Write a Python program to find the repeated items of a tuple.

tuple=(1,2,3,4,5,6,6,7,8,9,9)
print(tuple)
for i in range(0,len(tuple)):
    for j in range(i+1,len(tuple)):
        if tuple[i]==tuple[j]:
            print("repeated items:",tuple[i])
    
