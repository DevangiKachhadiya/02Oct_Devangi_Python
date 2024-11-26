#to check the current position of the file cursor using tell().
fl=open("new.txt","a")
print(fl.write("Hii"))
print(fl.tell())