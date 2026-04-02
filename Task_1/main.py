from src.services.customer_service import CustomerService
from src.services.customer_info_manager import CustomerInfoManager

def menu_list():

    status = True

    while status == True:
        print("\n\"\"\"Welcome to the HKMU Banking System\"\"\"")
        selection = input("Please select one of the options to proceed:\n1. Customer Data Management\n\n").strip()
    
        try:
            if selection == "1":
                cust_manage_menu_list()
                status = False


        except ValueError:
            print("Please enter a numeric value between 1 to 5")


Customer_service = CustomerService()

def cust_manage_menu_list():
    try:

        ID_False = False

        while(ID_False == False):
            while True:
                id = input("Please enter the Customer ID: ").strip()

                if len(id) != 8:
                    print("Invalid ID. Must be 8 characters.")
                else:
                    break
            
            #Check if the ID exists
            status = Customer_service.check_accountInfo(id)
            ID_False = status

            if status == False:
                print("The inputted ID does not exist in the records")
            else:
                print("The inputted ID exists in the records")
        
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
                    
                elif selection == "2":
                    print ("""
                        What would you like to edit?:
                        1. First Name
                        2. Last Name
                        3. Balance
                        4. Account Type
                    """)
                    selection_1 = input("Please enter your selection: ").strip()
                    CustomerInfoManager.CustomerInfoEdit(selection_1, account_id=id)
                    print("The Changes have been made")

                elif selection == "4":
                    menu_list()

            except ValueError:
                print("Please enter a numeric value between 1 to 5")

    except ValueError:
        print("Please enter the correct ID")



if __name__ == "__main__":
    menu_list()