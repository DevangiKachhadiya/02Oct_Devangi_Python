for i in range(int(input("Enter N: "))):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code: ",e)