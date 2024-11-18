from bbbb import load_customers, save_customers
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def withdraw():
    account_number = input("Enter account number: ").strip()
    amount = input("Enter withdrawal amount: ").strip()

    if not amount.isdigit():
        print("Invalid amount. Please enter a numeric value.")
        return

    amount = float(amount)
    customers = load_customers()

    if account_number in customers:
        if customers[account_number]["balance"] >= amount:
            customers[account_number]["balance"] -= amount
            save_customers(customers)
            print(f"{get_current_time()} - Withdrawal of {amount} successful.")
        else:
            print(f"{get_current_time()} - Insufficient balance.")
    else:
        print(f"{get_current_time()} - Account not found.")

def deposit():
    account_number = input("Enter account number: ").strip()
    amount = input("Enter deposit amount: ").strip()

    if not amount.isdigit():
        print("Invalid amount. Please enter a numeric value.")
        return
    
    amount = float(amount)
    customers = load_customers()

    if account_number in customers:
        customers[account_number]["balance"] += amount
        save_customers(customers)
        print(f"{get_current_time()} - Deposit of {amount} successful.")
    else:
        print(f"{get_current_time()} - Account not found.")

def view_balance():
    account_number = input("Enter account number: ").strip()
    customers = load_customers()

    if account_number in customers:
        print(f"{get_current_time()} - Balance: {customers[account_number]['balance']}")
    else:
        print(f"{get_current_time()} - Account not found.")
