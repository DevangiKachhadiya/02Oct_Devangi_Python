import re

n = int(input())
for i in range(0, n):
    try:
        a=(re.compile(input()))
        print(bool(a))
    except re.error:
        print('False')  