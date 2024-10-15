#Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.

def swap_first_two_chars(str1,str2):
    print(str1,str2)

    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 +" " + new_str2

string1="abcd"
string2="kbn"
result = swap_first_two_chars(string1,string2)
print(result)
