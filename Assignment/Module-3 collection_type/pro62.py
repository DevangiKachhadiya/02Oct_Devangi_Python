# Write a Python program to calculate surface volume and area of a cylinder
import math

def cylinder_volume(radius,hight):
    return math.pi * radius **2 * hight

def cylinder_surface(radius,hight):
    return math.pi * radius * (radius + hight)

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

volume = cylinder_volume(radius,height)
surface = cylinder_surface(radius,height)

print("volume of cylinder: ",volume)
print("surface area of cylinder: ",surface)

