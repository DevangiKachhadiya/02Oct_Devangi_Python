n=int(input("Enter a number: "))
for i in range(0,+1):
    '''if n%3==0 or n%5==0 or (n%3 or n%5)==0:
        print("yes")'''
    
    if n%3 == 0:
        print("divisible by 3")
    if n%5==0:
        print("divisible by 5")
    if n%3 or n%5 ==0 :
        print(" divisible by both 3 and 5")
    