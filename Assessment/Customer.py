import Banker

def withdraw_amount():
    customers = Banker.load_customers()
    account_number = input("Enter account number: ")
    if account_number not in customers:
        print("Account not found.")
        return
    amount = input("Enter amount to withdraw: ")
    if not amount.isdigit():
        print("Invalid amount.")
        return
    amount = float(amount)
    if customers[account_number]["balance"] >= amount:
        customers[account_number]["balance"] -= amount
        Banker.save_customers(customers)
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")


def deposit_amount():
    customers = Banker.load_customers()
    account_number = input("Enter account number: ")
    if account_number not in customers:
        print("Account not found.")
        return
    amount = input("Enter amount to deposit: ")
    if not amount.isdigit():
        print("Invalid amount.")
        return
    amount = float(amount)
    customers[account_number]["balance"] += amount
    Banker.save_customers(customers)
    print("Deposit successful.")


def view_balance():
    customers = Banker.load_customers()
    account_number = input("Enter account number: ")
    if account_number in customers:
        balance = customers[account_number]["balance"]
        print(f"Your current balance is: {balance}")
    else:
        print("Account not found.")
