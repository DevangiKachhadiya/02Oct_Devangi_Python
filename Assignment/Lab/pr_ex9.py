'''Write a Python program to handle file exceptions and use the 
finally block for closing the file.'''

try:
    fl=open("record.txt","r")
    print(fl.read())

except Exception as e:
    print(f"Error: {e}")

finally:
    fl.close()
    print("File is closed")

