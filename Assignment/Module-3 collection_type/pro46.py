#Write a Python program to combine values in python list of dictionaries.
'''Sample data: 
[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})'''

data=[
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount':300},
    {'item': 'item1', 'amount': 750}
    ]

combine_value={}

for i in data:
    item=i['item']
    amount=i['amount']

    if item in combine_value:
        combine_value[item] += amount
    else:
        combine_value[item] = amount

print(combine_value)
