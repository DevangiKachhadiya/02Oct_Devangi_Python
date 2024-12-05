'''WAP that demonstrates the correct use of indentation, comments, and
variables following PEP 8 guidelines.'''

def area_rectangle(length,width):
    return length*width

#input dimension
length=5  #length of rectangle
width=3   #width of rectangle

# calculate area
area=area_rectangle(length,width)

#display the result
print(f"The area of the rectangle is {area} square meter.")

'''length=int(input("Enter length of square: "))
width=int(input("Enter the width of square: "))

result=length*width

print(f"Square of area is:{result}")
'''