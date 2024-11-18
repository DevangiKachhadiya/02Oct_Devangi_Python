import os
import datetime

CUSTOMERS_FILE = "customers.txt"

def log_transaction(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{current_time} - {message}\n"
    with open("transactions.log", "a") as log_file:
        log_file.write(log_message)

'''def initialize_files():
    if not os.path.exists(CUSTOMERS_FILE):
        with open(CUSTOMERS_FILE, 'w') as f:
            pass'''

def load_customers():
    customers = {}
    with open(CUSTOMERS_FILE, 'r') as f:
        for line in f:
            if line.strip():
                account_number, name, balance = line.strip().split(',')
                customers[account_number] = {"name": name, "balance": float(balance)}
    return customers

def save_customers(customers):
    with open(CUSTOMERS_FILE, 'w') as f:
        for account_number, details in customers.items():
            f.write(f"{account_number},{details['name']},{details['balance']}\n")

def add_customer():
    name = input("Enter customer name: ").strip()
    account_number = input("Enter account number: ").strip()
    balance = input("Enter initial balance: ").strip()

    if not balance.isdigit():
        print("Invalid balance. Please enter a numeric value.")
        return
    
    balance = float(balance)
    customers = load_customers()

    if account_number in customers:
        print("Account number already exists. Please try again.")
        return

    customers[account_number] = {"name": name, "balance": balance}
    save_customers(customers)
    log_transaction(f"Customer added: {name}, Account Number: {account_number}, Balance: {balance}")
    print("Customer added successfully.")

def view_customer():
    account_number = input("Enter account number: ").strip()
    customers = load_customers()

    if account_number in customers:
        customer = customers[account_number]
        print(f"Customer Details: Name: {customer['name']}, Balance: {customer['balance']}")
        log_transaction(f"Viewed customer: {customer['name']}, Account Number: {account_number}")
    else:
        print("Customer not found.")
        log_transaction(f"Failed to view customer: Account Number {account_number} not found.")