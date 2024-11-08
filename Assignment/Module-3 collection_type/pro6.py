'''Write a Python program to count the number of strings where the string length is 2 or 
 more and the first and last character are same from a given list of strings.
'''
str=["hello" ,"refer","python","mam"]
#print(len(str))
count = 0
for i in str :
    if len(str) >= 2 and str[0] == str[-1] :
        count += 1
        print(count)

