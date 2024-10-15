#Write a Python function that takes a list of words and returns the length of the longest one.

sen = input("Enter sentence: ")
longest = max(sen.split(), key=len)
print("Longest word is: ", longest)
print("its length is: ", len(longest))
