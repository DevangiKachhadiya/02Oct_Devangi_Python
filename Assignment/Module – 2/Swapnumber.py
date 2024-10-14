#Write python program that swap two number with temp variable & without temp variable.

# swap two number with temp variable
a = 19
b = 10
print ( "before swap A : ",a)
print ( "before swap B : ",b)

temp = a
a = b
b = temp

print ( "after swap A : ",a)
print ( "after swap B : ",b)

# swap two number without temp variable.

A = 16
B = 27
print ( "before swap a : ",A)
print ( "before swap b : ",B)

A , B = B, A

print ( "after swap a : ",A)
print ( "after swap b : ",B)
