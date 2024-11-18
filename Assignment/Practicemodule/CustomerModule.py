from Banker1 import load_customers,save_customers
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def Withdraw_Amount():
    account_number=input("Enter account number: ").strip()
    amount=input("Enter Withdrawal amount: ").strip()

    if not amount.isdigit():
        print("Invalid choice.Enter numeric value")
        return
    amount=float(amount)
    customers=load_customers()
    
    if account_number in customers:
        if customers[account_number]["balance"] >= amount:
            customers[account_number]["balance"] -= amount
            save_customers(customers)
            print(f"{get_current_time()}-withdrawal of {amount}successfully ")
        else:
            print(f"{get_current_time()}-insufficient balance")
    else:
        print(f"{get_current_time()}-Account not found")

def Deposit_Amount():
    account_number=input("Enter account number: ").strip()
    amount=input("Enter Deposit amount: ").strip()

    if not amount.isdigit():
        print("Invalid choice.Enter numeric value")
        return
    amount=float(amount)
    customers=load_customers()

    if account_number in customers:
        customers[account_number]["balance"] += amount
        save_customers(customers)
        print(f"{get_current_time()}-Deposit of {amount}-successfully")
    else:
        print(f"{get_current_time()}-Account not found")

def View_Balance():
    account_number=input("Enter account number: ").strip()
    customers=load_customers()  
    if account_number in customers:
        print(f"{get_current_time()}-Balance:{customers[account_number]['balance']}")
    else:
        print(f"{get_current_time()}-Account not found")
        

    

