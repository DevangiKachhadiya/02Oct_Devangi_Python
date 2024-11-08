x = int(input("Enter value of X: "))
y = int(input("Enter value of Y: "))
z = int(input("Enter value of Z: "))

#if x>y or y>z or z>x:
if x>y and x>z:
    print("x is max")
elif y>z and y>x:
    print("y is max")
elif z>x and z>y:
    print("z is max")

