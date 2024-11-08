year = int(input("Enter year: "))
if year%4==0 or (year%100==0 and year%400==0):
    print("yes,this is leap year")
else:
    print("no,not leap year")