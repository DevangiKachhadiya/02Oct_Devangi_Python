#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sum_3 (x,y,z) :
    if x == y or y == z or x == z:
        return 0
    else:
        sum = x + y + z
        return sum
    
print(sum_3(2,3,5))
print(sum_3(2,2,5))
print(sum_3(1,0,1))
print(sum_3(3,6,9))


 
