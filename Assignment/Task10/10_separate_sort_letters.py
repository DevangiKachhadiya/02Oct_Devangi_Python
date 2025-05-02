#  Solve in Fewest Steps
'''Given a string consisting of letters and digits, write a Python program to separate and sort letters
and digits individually and then concatenate them, letters first and digits after, with each group
sorted individually.
'''

def solve_in_fewest_steps(s):
    letters = ''.join(sorted([char for char in s if char.isalpha()]))
    digits = ''.join(sorted([char for char in s if char.isdigit()]))
    return letters + digits

input_string = "B4A1D3"
print(solve_in_fewest_steps(input_string))