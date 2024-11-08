# Example-1
number=23
running=True

while running:
    guess = int(input("Enter a Number : "))
    if guess == number :
        print("Success")
        running = False
    elif guess < number:
        print("number is smaller than original")
    elif guess > number:
        print("Number is larger than original")
    else:
        print("sorry")
else:
    print("THe WHILE LOOP IS OVER")
print("Done")



# Example-2
i=0
while i < 7 :
    j=0
    while j < i :
        print(i, end =" ")
        j += 1
    i += 1
    print()
    