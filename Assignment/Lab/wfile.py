#Write a Python program to open a file in write mode, write some text, and then close it.

fl=open("writefile.txt","w")
fl.write("Hello every one this is vscode.\nIn this editor we can run python code.")
fl.write("\nIn VSCode we run multiple programming languages.")
print(fl)
fl.close()