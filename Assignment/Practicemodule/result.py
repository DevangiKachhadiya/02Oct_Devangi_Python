
sub1 = int (input("Enter subject1 mark : "))
sub2 = int (input("Enter subject2 mark : "))
sub3 = int (input("Enter subject3 mark : "))
sub4 = int (input("Enter subject4 mark : "))

total = sub1 + sub2 + sub3 + sub4
print("Total:",total)

per = total / 4
print ("Per:",per)

if per >= 70:
    print("Result : pass with Distiction")
elif per >= 60 :
    print("Result : pass with First class")
elif per >= 50 :
    print("Result : pass with Second class")
elif per >= 40 :
    print("Result :  pass class")
else:
    print("Result : Fail")