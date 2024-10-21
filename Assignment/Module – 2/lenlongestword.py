#Write a Python function that takes a list of words and returns the length of the longest one.

str = "Hi ,welcome to the python programming".split()

longest = 0
for word in str:
    if len(word) > longest:
        longest = len(word)
print(f"len of longest_word is: {longest}")
