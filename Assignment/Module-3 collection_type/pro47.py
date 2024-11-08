#Write a Python program to create a dictionary from a string.
'''Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

string='happy new year'
char_count = {}

for i in string:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

print(char_count)


   