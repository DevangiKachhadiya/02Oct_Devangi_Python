# Inventory Matching and Pricing
'''You have an inventory of products, each with a specific quantity and unit price. Customers place
orders with a budget. Write a Python program to:
• Determine if an order can be completely fulfilled within a customer's budget.
• Prioritize items based on available quantities and prices.
• Clearly state if the order is fulfillable, partially fulfillable, or impossible.
'''

def inventory_matching(order, inventory, budget):
    total_price = 0
    items_fulfilled = []
    
    inventory.sort(key=lambda x: x['price'])
    for item in inventory:
        if item['name'] in order and order[item['name']] <= item['quantity']:
            total_price += order[item['name']] * item['price']
            items_fulfilled.append(item['name'])
            if total_price > budget:
                return "Impossible"
    
    if set(order.keys()) == set(items_fulfilled):
        return f"Fulfillable within budget: {total_price}₹"
    return "Partially Fulfillable"

inventory = [
    {'name': 'item1', 'quantity': 10, 'price': 100},
    {'name': 'item2', 'quantity': 5, 'price': 200}
]
order = {'item1': 3, 'item2': 4}
budget = 1500
print(inventory_matching(order, inventory, budget))