# *****
# *****
# *****

for i in range(3): #Outerloop for lines
    for j in range(5): # inearloop for no. of stars
        print("*", end=' ')
    print('')

# Dynamic user input
n = int(input("Enter no of rows: "))
m = int(input("Enter number of columns: "))

for i in range(n):
    for j in range(m):
        print('*', end = '')
    print()