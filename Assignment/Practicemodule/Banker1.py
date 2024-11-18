import os
import datetime

CUSTOMERS_FILE="customers.txt"

def transactions(message):
    current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message=f"{current_time} - {message}\n"
    fl=open("transactions.log","a")
    fl.write(log_message)

def load_customers():
    customers={}
    f=open(CUSTOMERS_FILE,'r')
    for line in f:
        if line.strip():
            account_number,name,balance = line.strip().split(',')
            customers[account_number] = {"name":name,"balance":float(balance)}
    return customers

def save_customers(customers):
    f=open(CUSTOMERS_FILE,'w')
    for account_number,details in customers.items():
        f.write(f"{account_number},{details['name']},{details['balance']}\n")

def add_customer():
    name=input("Enter customer name: ").strip()
    account_number=input("Enter account number: ").strip()
    balance=input("Enter balance: ").strip()

    if not balance.isdigit():
        print("Invalid balance, Enter numeric value")
        return
    
    balance=float(balance)
    customers=load_customers()

    if account_number in customers:
        print("Account number is already exit")
        return
    customers[account_number]={"name":name,"balance":balance}
    save_customers(customers)
    transactions(f"Customer Added:{name},Account Number:{account_number},Balance:{balance}")
    print("Customer Added Successfully")

def view_customer():
    account_number=input("Enter account number: ").strip()
    customers=load_customers

    if account_number in customers:
        customer = customers[account_number]
        print(f"Customers Details:Name:{customer['name']},Balance:{customer['balance']}")
        transactions(f"Viewed Customer:{customer['name']},Account Number:{account_number}")

    else:
        print("Customer Not Found")
        transactions(f"failed to view customer:Account Number {account_number} Not Found")
