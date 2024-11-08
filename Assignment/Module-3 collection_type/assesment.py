# Python Bank Management System (Function-Based Version)
customers=[]
def add_customer(account_no,name,balance):
    customer={"Account Number":account_no,"Customer Name":name ,"Account Balance":balance}
    customers.append(customer)
    print(f"\nCustomer {name} added successfully.")

def view_customer(account_no):
    for customer in customers:
        if customer["account_no"] == account_no:
            print("Account No:" ,customer['account_no'])
            print("Customer Name:" ,customer['name'])
            print("Account Balance:" ,customer['balance'])
            return
    print("\nCustomer not found.")

def search_customer(name):
    found = False
    for customer in customers:
        if customer["name"].lower() == name.lower():
            print("Account No:" ,customer['account_no'])
            print("Customer Name:" ,customer['name'])
            print("Account Balance:" ,customer['balance'])
            found = True
    if not found:
        print("\nCustomer not found")

def view_all_customers():
    if not customers:
        print("\nNo customers in the bank") 
    else:
        print("\nAll Customers:")
        for customer in customers:
            print("Account No:" ,customer['account_no'])
            print("Customer Name:" ,customer['name'])
            print("Account Balance:" ,customer['balance'])

def total_amount_in_bank():
    total = sum(customer["balance"] for customer in customers)
    print("Total Amount in Bank:",total)

def banker_operations():
    while True:
        print("Welcome to Banker's App \nOperations Menu")
        print("1) Add Customer")
        print("2) view Customer")
        print("3) search Customer")
        print("4) View All Customers")
        print("5) Total Amounts in Bank")
        print("6) Exit to Main Menu")

        choice = input("Choose an operation: ")
        
        if choice == "1":
            account_no = int(input("Enter Account Number: "))
            name = input("Enter Customer Name: ")
            balance = float(input("Enter Balance: "))
            add_customer(account_no,name,balance)
        elif choice == "2":
            account_no = int(input("Enter Account Number To View: "))
            view_customer(account_no)
        elif choice == "3":
            name = input("Enter Customer Name To Search: ")
            search_customer(name)
        elif choice == "4":
            view_all_customers()
        elif choice == "5":
            total_amount_in_bank()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        print("\nWELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
        print("Select your role:")
        print("1) Banker")
        print("2) Customer")
        print("3) Exit")

        role = input("Choose your role: ")

        if role == "1":
            banker_operations()
        elif role == "2":
            print("customer ")
        elif role == "3":
            print("Exiting the system . GoodBye")
            break
        else:
            print("Invalid role,please try again.")

main()
