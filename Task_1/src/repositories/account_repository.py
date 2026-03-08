from src.models.account import Account

class AccountRepository:

    FILE_PATH = "data/Accounts.txt"

    #Reading from the text file

    @staticmethod
    def load_data():

        Accounts = []

        try: 
            with open(AccountRepository.FILE_PATH, "r") as file:
                for line in file:
                     id, first_name, last_name, balance, acc_type = line.strip().split(",")

                     Account_1 = Account(id, first_name, last_name, float(balance), acc_type) 

                     Accounts.append(Account_1)

        except FileNotFoundError:
            print("File not found")
        
        return Accounts

