def is_leap(year):
    leap = False

    # logic 
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        
    return leap

year = int(input("Enter a Year: "))
print(is_leap(year))
            