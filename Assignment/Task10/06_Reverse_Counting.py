# Reverse Counting
'''Write a Python program that prints numbers from 1000 down to 1 without using any loops (for,
while) or the any built-in functions like range().
'''

import sys
sys.setrecursionlimit(2000)

def reverse_count(n):
    if n == 0:
        return
    print(n)
    reverse_count(n - 1)

reverse_count(1000)