student=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    name=input("Enter name:  ")
    student.append(name)
print(set(student))
