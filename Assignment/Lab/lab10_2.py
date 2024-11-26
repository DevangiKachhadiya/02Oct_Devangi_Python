#WAP to match a word in a string using re.match().
import re
my_str="This is Python!"
x=re.match('This',my_str)
print(x)
if x:
    print("Match done!")
else:
    print("Error!")