# Write a Python program to read a random line from a file.

import random

f1=open("record.txt","r")

line=f1.read().splitlines()

print(random.choice(line))



