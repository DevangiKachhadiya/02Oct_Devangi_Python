

#Write a Python program to create a file and write a string into it.

open("newfile.txt","x")
print("File created Successfully")

fl=open("newfile.txt","w")
print(fl.write("this is text file.\nwe can save text file using .txt extension."))
