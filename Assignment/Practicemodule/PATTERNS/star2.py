# ****
# ***
# **
# *

n = int(input("Enter N: "))

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end = '')
    print()
