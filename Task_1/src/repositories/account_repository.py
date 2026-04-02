import os
from src.models.account import Account

class AccountRepository:

    BASE_DIR = os.path.dirname(__file__)

    FILE_PATH = os.path.abspath(
        os.path.join(BASE_DIR, "..", "..", "data", "accounts.txt")
    )

    @staticmethod
    def check_customer_id(account_id):
        try: 
            with open(AccountRepository.FILE_PATH, "r") as file:

                for line in file:
                    id, first_name, last_name, balance, acc_type = line.strip().split(",")

                    if id == account_id: 
                        return True 
                    
            return False

        except FileNotFoundError:
            print("File not found")
            print("Tried path:", AccountRepository.FILE_PATH)

    def load_customer_data(account_id):

        # Accounts = []

        try: 
            with open(AccountRepository.FILE_PATH, "r") as file:
                Loop_Status = True
                for line in file:
                    id, first_name, last_name, balance, acc_type = line.strip().split(",")

                    Account_1 = Account(id, first_name, last_name, float(balance), acc_type) 

                    if id == account_id:
                         print(Account_1.id + " " + Account_1.first_name + " " + str(Account_1.balance) + " " + Account_1.acc_type) 
                         Loop_Status = False   

                    if not Loop_Status:
                        break
                     
                    # Accounts.append(Account_1)

        except FileNotFoundError:
            print("File not found")
            print("Tried path:", AccountRepository.FILE_PATH)
        
    def edit_customer_data(account_id, input_1, selection_1):

        try: 
            with open(AccountRepository.FILE_PATH, "r") as file:
                lines = file.readlines()
            
            updated_lines = []
            
            for line in lines:
                id, first_name, last_name, balance, acc_type = line.strip().split(",")

                selection_1 = int(selection_1)

                if str(id) == str(account_id):
                    print("Match Found")

                    if selection_1 == 1:
                        first_name = input_1

                    elif selection_1 == 2:
                        last_name = input_1

                    elif selection_1 == 3:
                        balance = str(input_1)

                    elif selection_1 == 4:
                        acc_type = input_1

                updated_lines.append(f"{id},{first_name},{last_name},{balance},{acc_type}\n")
            
            with open(AccountRepository.FILE_PATH, "w") as file:
                file.writelines(updated_lines)

        except FileNotFoundError:
            print("File not found")
            print("Tried path:", AccountRepository.FILE_PATH)

