# open("file_operations.txt","x")

fl=open("file_operations.txt","w")
fl.write("Welcome to the python programming\nhello students")
print(fl)

fl=open("file_operations.txt","r")
print(fl.read())

fl=open("file_operations.txt","a")
print(fl.write("\nPython is easy to learn"))

fl=open("file_operations.txt","r+")
print(fl.read())
print(fl.write("\nAdd data after read file"))

fl=open("file_operations.txt","w+")
print(fl.write("\nall file operations done"))
print(fl.read())