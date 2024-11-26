#Write a Python program to write multiple strings into a file.

fl=open("wms.txt","w")
fl.writelines("Hello,Everyone!!!\nGood Morning\nHow Are You All Today???")
print(fl)
