# Date Difference Calculator
'''
Write a Python program that calculates the difference between two dates provided by a user.
Scenario Example:
A user wants to find out how many days they've lived by inputting their birthdate and today's date.
Your program should:
• Take two dates as input (format: dd-mm-yyyy).
• Output the difference in days clearly.
'''

from datetime import datetime

def date_difference(date1, date2):
    date_format = "%d-%m-%Y"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return (d2 - d1).days

birthdate = input("Enter birthdate (dd-mm-yyyy): ")
today = input("Enter today's date (dd-mm-yyyy): ")
days_lived = date_difference(birthdate, today)
print(f"You've lived {days_lived} days.")
