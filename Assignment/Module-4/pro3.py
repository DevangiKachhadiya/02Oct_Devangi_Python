#Write a program to append text to a file and display the text.

open("append.txt","a")

fl=open("append.txt","a")

print("python is very popular")
print(fl.write("python is very popular"))