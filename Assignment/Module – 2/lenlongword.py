#Write a Python function that takes a list of words and returns the length of the longest one.

str = input("enter a string :")
longest=max(str.split(),key=len)
print("longest word is:",longest)
print("length is:",len(longest))
