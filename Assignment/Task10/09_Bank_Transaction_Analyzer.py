#  Bank Transaction Analyzer
'''Write a Python program that allows users to input a series of transactions (credits and debits). Your
program should:
• Record each transaction clearly.
• Calculate and print the balance after each transaction.
• Provide a final summary at the end.
'''

def bank_transaction_analyzer(transactions):
    balance = 0
    for transaction in transactions:
        balance += transaction
        print(f"Transaction: {transaction} | Balance: {balance}")
    print(f"Final balance: {balance}")

transactions = [1000, -500, -200, 300]
bank_transaction_analyzer(transactions)