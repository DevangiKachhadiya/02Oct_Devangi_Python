import Banker1
import Customer

def select_role():
    print("\nselect your role\n1)Banker\n2)Customer\n3)Exit\n")

def get_banker_Operations():
    print("\nOperations Menu\n1)Add Customer\n2)View Customer\n3)Search Customer\n4)View All Customer\n5)Total Amounts in Bank\n6)Back to Main Menu\n")

def get_customer_Operations():
    print("\nOperations Menu\n1)Withdraw Amount\n2)Deposit Amount\n3)View Balance\n")

def ask_continue():
    while True:
        choice = input("Do you want to perform more operations press 'y' for yes and press 'n' for no : ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid input, Please enter 'y' for continue and 'n' for exit")


def main():
    while True:
        select_role()
        choice=input("Choose your role: ").strip()

        if choice==1:
             while True:
                get_banker_Operations()
                banker_choice=input("Enter operation which you want to perform: ").strip()

                if banker_choice=='1':
                   Banker1.add_customer()
                elif banker_choice=='2':
                    Banker1.view_customer()
                elif banker_choice=='3':
                    Banker1.search_customer()
                elif banker_choice=='4':
                    Banker1.view_all_customer()
                elif banker_choice=='5':
                    Banker1.total_amount_in_bank()
                elif banker_choice=='6':
                    break
                else:
                    print("Invalid choice,try again")

                if ask_continue() == 'n':
                    print("Exit the application")
                    return
        
        elif choice == '2':
            while True:
                get_customer_Operations()
                customer_choice=input("Enter operation which you want to perform: ").strip()

                if customer_choice=='1':
                    Customer.Withdraw_Amount()
                elif customer_choice=='2':
                    Customer.Deposit_Amount()
                elif customer_choice=='3':
                    Customer.View_Balance()
                elif customer_choice=='4':
                    break
                else:
                    print("Invalid choice,try again")

                if ask_continue() =='n':
                    print("Exit the application")
                    return
                
        elif choice=='3':
            print("Exit the application")
            return
        else:
            print("Invalid choice,try again")
    
        if ask_continue()=='n':
            print("Exit the application")
            break

if __name__=="_main_":
    main()
    


    
        

