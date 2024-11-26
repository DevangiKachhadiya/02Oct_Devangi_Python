try:
    num=int(input("Enter any number:"))
    ans=10/num

except Exception as e:
    print(f"Error Occurred: {e}")
finally:
    print("completed successfully")