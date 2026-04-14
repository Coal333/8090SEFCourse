from src.services.customer_service import CustomerService
from src.services.customer_info_manager import CustomerInfoManager
from src.services.business_service import BusinessService

import random

Customer_Service = CustomerService()
Business_Service = BusinessService()

def menu_list():

    status = True

    while status == True:
        print("\n\"\"\"Welcome to the HKMU Banking System\"\"\"")
        selection = input("Please select one of the options to proceed:\n1. Customer Data Management\n").strip()
    
        try:
            if selection == "1":
                cust_manage_menu_list()
                status = False

        except ValueError:
            print("Please enter a numeric value between 1 to 5")

def cust_manage_menu_list():
    try:

        loop_status= True

        while loop_status:

            id = input("Please enter the Customer ID: ").strip()

            while True: 
                if len(id) != 8:
                    print("Invalid ID. Must be 8 characters.")
                    continue
                else:
                    break

            #Check if the ID exists

            status = Customer_Service.check_accountInfo(id)
            
            if status == False:
                print("The inputted ID does not exist in the records")
                
            else:
                print("The inputted ID exists in the records")
                loop_status = False

        customer_type = ""

        id_text = list(id)
        first_char = id_text[0]

        if first_char == "A":
            customer_type = "Standard"
        else:  
            customer_type = "Business"

        B_A_Status_Key = ""

        if customer_type == "Business":

            status_1 = True
            state_3 = False

            while status_1 == True:

                print ("""
                    Please select one of the options to proceed:
                    1. Access the Customer Management Menu
                    2. Access the Contract Managment Menu
                    3. Generate Today's random color
                """)
                selection = input("Please enter your selection: ").strip()

                if selection == "1":
                    
                    B_A_Status_Key = "Customer_M_M"
                    break
                    
                elif selection == "2":

                    B_A_Status_Key = "Contract_M_M"
                    break

                else:
                  
                    if state_3 == False:
                        num = random.random()
                        color = ""

                        if 0.8 <= num < 1:
                            color = "Red"

                        elif 0.6 <= num < 0.8:
                            color = "Blue"

                        elif 0.4 <= num < 0.6:
                            color = "Green"
                        
                        elif 0.2 <= num < 0.4:
                            color = "Yellow"
                        
                        else:
                            color = "Orange"

                        print(f"Today's random color is {color}")

                        state_3 = True

                    else:

                        print(f"Today's random color was already shown before, it was {color}")

        print("\"\"\"Customer Account Menu\"\"\"")

        if customer_type == "Standard" or B_A_Status_Key == "Customer_M_M":

            status = True
            while status == True:
                print ("""
                    Please select one of the options to proceed:
                    1. View Customer Information
                    2. Edit Customer Information
                    3. Transfer Money
                    4. Go back to the first page
                        """)
                selection = input("Please enter your selection: ").strip()
                
                
                if selection == "1":
                    
                    print("Account Information: ")
                    Customer_Service.get_accountInfo(account_id=id)
                    
                elif selection == "2":

                    print ("""
                        What would you like to edit?:
                        1. First Name
                        2. Last Name
                        3. Current Balance
                        4. Checking Balance
                        5. Account Type
                    """)
                    selection_1 = input("Please enter your selection: ").strip()
                    CustomerInfoManager.CustomerInfoEdit(selection_1, account_id=id)
                    print("The Changes have been made")

                if selection == "3":

                    print("Transfer Money: ")
                    Customer_Service.transfer_money(account_id=id)
                    print("The money has been transferred")

                elif selection == "4":

                    menu_list()

        if B_A_Status_Key == "Contract_M_M":

            status = True
            while status == True:
                print ("""
                    Please select one of the options to proceed:
                    1. View all Contracts
                    2. Create a new Contract
                    3. Delete all Contracts
                    4. Go back to the first page
                        """)
                selection = input("Please enter your selection: ").strip()

                if selection == "1":
                    
                    print("View all Contracts:\n")
                    Business_Service.get_allContracts(account_id=id)

                elif selection == "2":

                    Business_Service.create_newContract(account_id=id)
                    print("The contract has been saved\n")

                elif selection == "3":

                    Business_Service.delete_allContracts(account_id=id)
                    print("All the records have been deleted\n")

                elif selection == "4":

                    menu_list()

    except ValueError:
        print("Please enter the correct ID")

if __name__ == "__main__":
    menu_list()