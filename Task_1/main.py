from src.services.customer_service import CustomerService

def menu_list():

    status = True

    while status == True:
        print("\"\"\"Welcome to the HKMU Banking System\"\"\"")
        selection = input("Please select one of the options to proceed:\n1. Customer Data Management\n").strip()
    
        try:
            if selection == "1":
                cust_manage_menu_list()
                status = False


        except ValueError:
            print("Please enter a numeric value between 1 to 5")


Customer_service = CustomerService()

def cust_manage_menu_list():
    try:
        id = str(input("Please enter the Customer ID: "))

        if len(id) !=8:
            raise ValueError
        
        print("\"\"\"Customer Account Menu\"\"\"")

        status = True

        while status == True:
            print ("""
                Please select one of the options to proceed:
                1. View Customer Information
                2. Edit Customer Information
                3. Transfer Money
                4. Go back to the previous Menu
                    """)
            selection = input("Please enter your selection: ").strip()
    
            
            try:
                if selection == "1":
                    
                    print("Account Information: ")
                    Customer_service.get_accountInfo(account_id=id)
                    

                elif selection == "4":
                    break

            except ValueError:
                print("Please enter a numeric value between 1 to 5")

    except ValueError:
        print("Please enter the correct ID")





if __name__ == "__main__":
    menu_list()