import os
from src.models.business_account import Business_Account
from src.models.customer_account import Customer_Account

#Account Repository Class that manages account data (Storing and Retrieving data)
class AccountRepository:

    BASE_DIR = os.path.dirname(__file__)

    FILE_PATH = os.path.abspath(
        os.path.join(BASE_DIR, "..", "..", "data", "accounts.txt")
    )

    @staticmethod
    #checking whether the id exists in the database
    def check_customer_id(account_id):

        try: 
            with open(AccountRepository.FILE_PATH, "r") as file:

                for line in file:
                    id, A, B, balance_current, balance_checking, acc_type = line.strip().split(",")

                    #if id exists return True
                    if str(id).strip() == str(account_id).strip():
                        return True 
                    
            return False

        except FileNotFoundError:
            print("File not found")

    #loading customer record data
    def load_customer_data(account_id):

        # Accounts = []

        try: 
            with open(AccountRepository.FILE_PATH, "r") as file:
                Loop_Status = True
                for line in file:

                    #save each value in to the following variables
                    id, A, B, balance_current, balance_checking, acc_type = line.strip().split(",")

                    id_text = list(id)
                    first_char = id_text[0]

                    #Standard accounts
                    if first_char == "A":
                        customer_type = "Standard"
                        id, fist_name, last_name, balance_current, balance_checking, acc_type = line.strip().split(",")
                    #business accounts
                    else:  
                        customer_type = "Business"
                        id, company_name, company_type, balance_current, balance_checking, acc_type = line.strip().split(",")

                    if customer_type == "Standard":
                        Account_1 = Customer_Account(id, fist_name, last_name, float(balance_current), float(balance_checking), acc_type) 
                    else:
                        Account_1 = Business_Account(id, company_name, company_type, float(balance_current), float(balance_checking), acc_type) 

                    #printing section
                    if str(id).strip() == str(account_id).strip():
                         
                        if customer_type == "Standard":
                            print(Account_1.id + " " + Account_1.first_name + " " + str(Account_1.balance_current) + " " + str(Account_1.balance_checking) + " " + Account_1.acc_type + "\n") 
                            Loop_Status = False   
                        else:
                            print(Account_1.id + " " + Account_1.company_name + " " + str(Account_1.balance_current) + " " + str(Account_1.balance_checking) + " " + Account_1.acc_type + "\n") 
                            Loop_Status = False 
                        
                    if not Loop_Status:
                        break
                     
                    # Accounts.append(Account_1)

        except FileNotFoundError:
            print("File not found")
    
    #editing account data
    def edit_customer_data(account_id, input_1, selection_1):

        try: 
            with open(AccountRepository.FILE_PATH, "r") as file:
                lines = file.readlines()
            
            updated_lines = []
            selection_1 = int(selection_1)
            
            for line in lines:
                id, first_name, last_name, balance_current, balance_checking, acc_type = line.strip().split(",")

                #number selection allows correct variable's value to be changed by the user
                if str(id).strip() == str(account_id).strip():

                    #Editing first name, company name
                    if selection_1 == 1:
                        first_name = input_1

                    #Editing lastname, business type
                    elif selection_1 == 2:
                        last_name = input_1

                    #Editing current balance
                    elif selection_1 == 3:
                        balance_current = str(input_1)

                    #Editing checking balance
                    elif selection_1 == 4:
                        balance_checking = str(input_1)

                    #Editing account type
                    elif selection_1 == 5:
                        acc_type = input_1

                updated_lines.append(f"{id},{first_name},{last_name},{balance_current},{balance_checking},{acc_type}\n")
            
            with open(AccountRepository.FILE_PATH, "w") as file:
                file.writelines(updated_lines)

        except FileNotFoundError:
            print("File not found")

    #transferring money section
    def transfer_money(account_id, send_to_id, choice, amount):

        try: 
            with open(AccountRepository.FILE_PATH, "r") as file:
                lines = file.readlines()

            updated_lines = []
            choice = int(choice)

            for line in lines:
                id, first_name, last_name, balance_current, balance_checking, acc_type = line.strip().split(",")

                balance_current = float(balance_current)
                balance_checking = float(balance_checking)

                #Updating the sender account's balances
                if str(id).strip() == str(account_id).strip():

                    if choice == 1:
                        balance_current -= amount
                        balance_current = str(balance_current)

                    elif choice == 2:
                        balance_checking -= amount
                        balance_checking = str(balance_current)
                                        
                    print("Updated Record:", id, balance_current, balance_checking)

                #Adding data in to the list
                updated_lines.append(f"{id},{first_name},{last_name},{balance_current},{balance_checking},{acc_type}\n")
            
            with open(AccountRepository.FILE_PATH, "w") as file:
                file.writelines(updated_lines)

            updated_lines = []

            for line in lines:
                id, first_name, last_name, balance_current, balance_checking, acc_type = line.strip().split(",")

                balance_current = float(balance_current)
                balance_checking = float(balance_checking)

                #Updating the receiver account's balances
                if str(id).strip() == str(send_to_id).strip():

                    if choice == 1:
                        balance_current += amount
                        balance_current = str(balance_current)

                    elif choice == 2:
                        balance_checking += amount
                        balance_checking = str(balance_current)

                    print("Updated Record:", send_to_id, balance_current, balance_checking)
                
                #Adding data in to the list
                updated_lines.append(f"{id},{first_name},{last_name},{balance_current},{balance_checking},{acc_type}\n")

            with open(AccountRepository.FILE_PATH, "w") as file:
                file.writelines(updated_lines)

        except FileNotFoundError:
            print("File not found")