#Write a Python program to find the first appearance of the substring'not' and 'poor' 
#from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' 
#substring with 'good'. Return the resulting string.


str=input("enter a string: ")
x=str.replace('not poor','good')
print(x)