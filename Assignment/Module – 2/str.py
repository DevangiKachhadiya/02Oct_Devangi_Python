#Write a Python program to get a single string from two given strings,separated by a 
# space and swap the first two characters of each string.
s1="Hello Every one  "
s2="nice to meet you "
s3=s1+s2

print(s3)
new_s1=s2[:2]+s1[2:]
new_s2=s1[:2]+s2[2:]
print(new_s1 + "  " + new_s2)
new_str=(s1,s2)







