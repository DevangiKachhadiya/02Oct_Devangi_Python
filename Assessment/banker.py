#import datetime
#print("\n WELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
#print("\n select your role: ")
customers = [ ]
def add_customer(acc_no,name,balance):
    customer = {"Account_No":acc_no,"Customer_Name":name,"Opening_Balance":balance}
    customers.append(customer)
    print("f\nCustomer {name} add successfully")

def view_customer(acc_no):
    for customer in customers:
        print("Account_No:",customer['acc_no'])
        print("Customer_Name:",customer['name'])
        print("Opening_Balance:",customer['balance'])
        return
    print("\nCustomer not found")

def search_customer(name):
    found = False
    for customer in customer:
        if customer["name"].lower()==name.lower():
            print("Account_No:",customer['acc_no'])
            print("Customer_Name:",customer['name'])
            print("Opening_Balance:",customer['balance'])
            found=True
        if not found:
            print("customer not found")

def view_all_customer():
    if not customers:
        print("No Customers in the bank")
    else:
        print("All Customers: ")
        for customer in customers:
            print("Account_No:",customer['acc_no'])
            print("Customer_Name:",customer['name'])
            print("Opening_Balance:",customer['balance'])

def total_amount_in_bank():
    total = sum(customer["balance"])
    for customer in customers:
        print("Total Amount in Bank: ",total)


def banker_operations():
    while True:
        print("Welcome to Banker's App \nOperations Menu")
        print("1) Add Customer")
        print("2) view Customer")
        print("3) search Customer")
        print("4) View All Customers")
        print("5) Total Amounts in Bank")

        choice = int(input("Enter Operation which you want to perform: "))
        if choice == 1:
            acc_no=int(input("Enter an Account No: "))
            name=input("Enter a Customer Name: ")
            balance=float(input("Enter a Opening Balance: "))
            add_customer(acc_no,name,balance)

        elif choice == 2:
            acc_no=int(input("Enter an Account No to view: "))
            view_customer(acc_no)

        elif choice == 3:
            name=input("Enter a Customer Name to search: ")
            search_customer(name)

        elif choice == 4:
            view_all_customer()

        elif choice == 5:
            total_amount_in_bank()
            break
        
        else:
            print("Invalid choice")

def statements():
    while True:
        print("\n WELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
        print("select your role: ")
        print("1)Banker")
        print("2)Customer")
        print("3)Exit")

        roll = int(input("choose your role: "))
        if roll == 1:
            banker_operations()
        elif roll == 2:
            print("customer_operations")
        elif roll == 3:
            print("Exit system")
            break
        else:
            print("InValid Role: ")

statements()

    
'''print("Account_No:",acc_no)
    print("Customer_Name:",name)
    print("Opening_Balance:",balance)

no=int(input("Enter an Account No: "))
name=input("Enter a Customer Name: ")
bal=int(input("Enter a Opening Balance: "))

add_customer(no,name,bal)
'''

'''def view_customer(id,name,balance,OpeningDate):
    print("Id:",id)
    print("Name:",name)
    print("Balance:",balance)
    print("openingDate:",OpeningDate)

cus_id=int(input("Enter any Id: "))
cus_nm=input("Enter Name: ")
bank_balance=int(input("Enter bank balance: "))
date=datetime.timezone()

view_customer(cus_id,cus_nm,bank_balance,date)


#def search_customer():
#def view_all_customer():
#def total_amounts_in_bank():'''