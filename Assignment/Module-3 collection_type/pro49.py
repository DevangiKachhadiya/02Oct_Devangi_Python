# Write a Python function to check whether a number is in a given range.
def is_in_range(num,start,end):
    return start <= num <= end

num=10
start=1
end=50

if is_in_range(num,start,end):
    print("Number is in range")
else:
    print("Number is not in range")
