# Write a Python program to calculate the area of a trapezoid.
def trapezoid_area(a,b,h):
    area = 0.5*(a+b)*h
    return area

a=float(input("Enter the length of first parallel side (a): "))
b=float(input("Enter the length of second parallel side (b): "))
h=float(input("Enter the height of trapezoid (h): "))

area = trapezoid_area(a,b,h)
print("area of trapezoid is:",area)
