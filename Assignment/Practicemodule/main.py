import bbbb
import cccc

def display_main_menu():
    print("""
Main Menu:
1. Bank Operations
2. Customer Operations
3. Exit
""")

def display_bank_menu():
    print("""
Bank Operations:
1. Add Customer
2. View Customer
3. Search Customer
4. View All Customers
5. View Total Amount in Bank
6. Back to Main Menu
""")

def display_customer_menu():
    print("""
Customer Operations:
1. Withdraw Amount
2. Deposit Amount
3. View Balance
4. Back to Main Menu
""")

def ask_continue():
    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid input. Please enter 'y' to continue or 'n' to exit.")

def main():
    bbbb.initialize_files()

    while True:
        display_main_menu()
        main_choice = input("Enter your choice: ").strip()

        if main_choice == '1':  # Bank Operations
            while True:
                display_bank_menu()
                bank_choice = input("Enter your choice: ").strip()

                if bank_choice == '1':
                    bbbb.add_customer()
                elif bank_choice == '2':
                    bbbb.view_customer()
                elif bank_choice == '3':
                    bbbb.search_customer()
                elif bank_choice == '4':
                    bbbb.view_all_customers()
                elif bank_choice == '5':
                    bbbb.view_total_balance()
                elif bank_choice == '6':
                    break  # Back to Main Menu
                else:
                    print("Invalid choice. Please try again.")

                if ask_continue() == 'n':
                    print("Exiting the application. Goodbye!")
                    return

        elif main_choice == '2':  # Customer Operations
            while True:
                display_customer_menu()
                customer_choice = input("Enter your choice: ").strip()

                if customer_choice == '1':
                    cccc.withdraw()
                elif customer_choice == '2':
                    cccc.deposit()
                elif customer_choice == '3':
                   cccc.view_balance()
                elif customer_choice == '4':
                    break  # Back to Main Menu
                else:
                    print("Invalid choice. Please try again.")

                if ask_continue() == 'n':
                    print("Exiting the application. Goodbye!")
                    return

        elif main_choice == '3':  # Exit
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

        if ask_continue() == 'n':
            print("Exiting the application. Goodbye!")
            break

if __name__ == "_main_":
    main()