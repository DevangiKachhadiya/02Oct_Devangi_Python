str = input("Enter a string: ")
revstr = " "

for i in str:
    revstr = i+revstr

if str==str[::-1]:
    print("str is palindrom")
else:
    print("str is not palindrom") 