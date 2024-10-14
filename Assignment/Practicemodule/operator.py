sub1 = int (input("Enter subject1 mark : "))
sub2 = int (input("Enter subject2 mark : "))
sub3 = int (input("Enter subject3 mark : "))
sub4 = int (input("Enter subject4 mark : "))

if sub1>=40 and  sub2>=40 and sub3>=40 and sub4 >=40 :

    total = sub1 + sub2 + sub3 + sub4
    print("Total:",total)

    per = total / 4 
    print ("Per:",per)

    if per >= 70 :
        print("Result : pass with Distinction")
    elif per >= 60 :
        print("Result : pass with First class")
    elif per >= 50 :
        print("Result : pass with Second class")
    elif per >= 40 :
        print("Result :  pass class")
    #else:
      #  print("Result : Fail")

else:
    print("Result Fail")