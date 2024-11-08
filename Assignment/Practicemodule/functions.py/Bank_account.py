balance = 0
def bank_account_opening(acc_holder_name, acc_type, acc_number):
    print("Account Holder Name:", acc_holder_name)
    print("Account Type:", acc_type)
    print("Account Number:", acc_number)

def deposit(balance):
    deposits = int(input("Enter your deposit amount: "))
    balance += deposits
    print("Your balance has been deposited successfully.")
    print(f"New balance: {balance}")
    return balance

def withdrawal(balance):
    amount = int(input("Enter your withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
        print(f"New balance after withdrawal: {balance}")
    else:
        print("Insufficient balance for withdrawal.")
    return balance

acc_holder_name = input("Enter account holder name: ")
acc_type = input("Enter account type: ")
acc_number = int(input("Enter account number: "))

bank_account_opening(acc_holder_name, acc_type, acc_number)

balance = deposit(balance)
balance = withdrawal(balance)

print("\nStatement")
print("Account Holder Name:", acc_holder_name)
print("Account Type:", acc_type)
print("Account Number:", acc_number)
print("Total Balance:", balance)
