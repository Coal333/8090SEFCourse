import os
from src.models.account import Account

class AccountRepository:

    BASE_DIR = os.path.dirname(__file__)

    FILE_PATH = os.path.abspath(
        os.path.join(BASE_DIR, "..", "..", "data", "accounts.txt")
    )

    @staticmethod
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
        

