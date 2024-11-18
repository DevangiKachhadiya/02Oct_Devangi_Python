import Banker
import Customer

def main():
    while True:
        print("\n\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
        print("\n\tSelect your role\n")
        print("\t1) Banker")
        print("\t2) Customer")
        print("\t3) Exit")
        choice = input("\nChoose your role: ")

        if choice == "1":
            while True:
                print("\n Welcome to Banker's App")
                print("\n\tOperations Menu\n")
                print("\t1) Add Customer")
                print("\t2) View Customers")  
                print("\t3) Search Customer") 
                print("\t4) View All Customers")
                print("\t5) Total Amount In Bank")
                print("\t6) Back to Main Menu")
                banker_choice = input("\nEnter operation which you want to perform: ")

                if banker_choice == "1":
                    Banker.add_customer()
                elif banker_choice == "2":  
                    Banker.view_customers()
                elif banker_choice == "3": 
                    Banker.search_customer()
                elif banker_choice == "4":  
                    Banker.view_all_customers()
                elif banker_choice == "5":
                    Banker.view_total_balance()
                elif banker_choice == "6":
                    break 
                else:
                    print("Invalid choice.")

        elif choice == "2":
            while True:
                print("Welcome to Customer's App")
                print("\n\tOperations Menu:")
                print("\n\t1) Withdraw Amount")
                print("\t2) Deposit Amount")
                print("\t3) View Balance")
                print("\t4) Back to Main Menu")
                customer_choice = input("Enter operation which you want to perform: ")

                if customer_choice == "1":
                    Customer.withdraw_amount()
                elif customer_choice == "2":
                    Customer.deposit_amount()
                elif customer_choice == "3":
                    Customer.view_balance()
                elif customer_choice == "4":
                    break 
                else:
                    print("Invalid choice.")

        elif choice == "3":
            print("Exiting program.")
            break  
        else:
            print("Invalid choice.")

main()
