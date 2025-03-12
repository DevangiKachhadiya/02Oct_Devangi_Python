'''
1
13
135
1357
'''

n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,2*i,2):
        print(j, end='')
    print()