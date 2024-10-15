# Write a Python function to reverses a string if its length is a multiple of 4.

str = input("Enter a String : ")
if len(str) %4 == 0 :
    print(''.join(reversed(str)))
else:
    print(str)

