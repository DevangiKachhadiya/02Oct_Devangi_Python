# 1
# 12
# 123
# 1234

n = int(input("Enter n: "))

for i in range(n+1):
    for j in range(i):
        print(j+1, end='')
    print()