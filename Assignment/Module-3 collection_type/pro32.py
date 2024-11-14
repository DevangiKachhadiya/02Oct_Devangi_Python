# Write a Python script to sort (ascending and descending) a dictionary by value.

import operator  
sub_score={'js':90,'maths':80,'python':89,'c':84,'html':99}

x=sorted(sub_score.items(),key=operator.itemgetter(1))
print("Ascending dict:",x)
y=sorted(sub_score.items(),key=operator.itemgetter(1),reverse=True)
print("Descending dict:",y)
