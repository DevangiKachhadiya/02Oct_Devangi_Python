# Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(string):
    if string==string[::-1]:
        return("string is palindrome")
    else:
        return("string is not palindrome")
    
string=input("Enter a String: ")
print(is_palindrome(string))


