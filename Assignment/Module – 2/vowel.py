#Write a Python program to test whether a passed letter is a vowel or not.

char = input("Enter any character : ")

vowels = ['a','e','i','o','u','A','E','I','O','U']

if char in vowels :
    print(f"The Character '{char}' is a Vowel")
else :
    print(f"The Character '{char}' is a Not Vowel it's a Consonant")
