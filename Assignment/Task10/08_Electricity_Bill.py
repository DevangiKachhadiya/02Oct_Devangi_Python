# Electricity Bill Calculation 
'''
An electricity provider charges consumers based on slabs of electricity usage:
Usage (kWh) Price per unit ( )₹
0-100 5
101-300 7
301-500 10
Above 500 15
Write a Python program that:
• Accepts electricity usage (in kWh) from the user.
• Clearly calculates and displays the bill, explaining the charges for each slab separately.
'''

def electricity_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 500:
        bill = 100 * 5 + 200 * 7 + (units - 300) * 10
    else:
        bill = 100 * 5 + 200 * 7 + 200 * 10 + (units - 500) * 15
    return bill

units = 450
print(f"Total electricity bill for {units} kWh is {electricity_bill(units)}₹")