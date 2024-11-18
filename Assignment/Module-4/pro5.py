#Write a Python program to read last n lines of a file.
fl=open("data.txt","r")
print(fl.readlines()[-1])
