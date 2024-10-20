#Write a Python program to test whether a passed letter is a vowel or not.

x = input("Enter any character : ")
vowels ='a','e','i','o','u','A','E','I','O','U'

if x in vowels :
    print(f"Character {x} is a Vowel")
else :
    print(f"Character {x} is a Not Vowel")
