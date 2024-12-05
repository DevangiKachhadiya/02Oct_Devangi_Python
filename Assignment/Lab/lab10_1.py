# WAP to search for a word in a string using re.search().
import re

my_str="This is Python!"
x=re.search('Python',my_str)
print(x)
if x:
    print("Match done!")
else:
    print("Error!")