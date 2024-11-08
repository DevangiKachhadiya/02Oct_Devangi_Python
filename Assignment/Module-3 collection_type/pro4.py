#Write a Python function to get the largest number, smallest num and sum of all from a list.

my_list=[1,2,3,4,5,6,7,8,9,10]
largest=max(my_list)
smallest=min(my_list)
sum=0   
for i in my_list:
    sum+=i
print("sum of my_list:",sum)
print("Largest num is :",largest)
print("smallest num is:",smallest)


   