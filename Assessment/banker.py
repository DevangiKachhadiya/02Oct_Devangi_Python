def load_customers():
    try:
        with open("customers.txt", "r") as file:
            customers = {}
            for line in file:
                if line.strip():  
                    account_number, name, balance = line.strip().split(",")
                    customers[account_number] = {"name": name, "balance": float(balance)}
            return customers
    except Exception as e:
        return {}  

def save_customers(customers):
    with open("customers.txt", "w") as file:
        for account_number, details in customers.items():
            file.write(f"{account_number},{details['name']},{details['balance']}\n")

def add_customer():
    customers = load_customers()
    account_number = input("Enter account number: ")
    if account_number in customers:
        print("Account number already exists.")
        return
    name = input("Enter customer name: ")
    balance = input("Enter initial balance: ")
    if not balance.isdigit():
        print("Invalid balance. Must be a number.")
        return
    customers[account_number] = {"name": name, "balance": float(balance)}
    save_customers(customers)
    print("Customer added successfully.")

def view_all_customers():
    customers = load_customers()
    if not customers:
        print("No customers found.")
    else:
        print("\nList of All Customers:")
        for acc_no, details in customers.items():
            print(f"Account: {acc_no}, Name: {details['name']}, Balance: {details['balance']}")

def view_customers():
    account_number = input("Enter account number to view: ")
    customers = load_customers()
    if account_number in customers:
        details = customers[account_number]
        print(f"Account: {account_number}, Name: {details['name']}, Balance: {details['balance']}")
    else:
        print("Customer not found.")

def search_customer():
    account_number = input("Enter account number: ")
    customers = load_customers()
    if account_number in customers:
        details = customers[account_number]
        print(f"Account: {account_number}, Name: {details['name']}, Balance: {details['balance']}")
    else:
        print("Customer not found.")

def view_total_balance():
    customers = load_customers()
    total = sum(cust["balance"] for cust in customers.values())
    print(f"Total balance in the bank: {total}")
