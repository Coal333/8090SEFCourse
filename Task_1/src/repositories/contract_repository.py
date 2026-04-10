import os
from src.models.contract import Contract

class ContractRepository:

    BASE_DIR = os.path.dirname(__file__)

    FILE_PATH = os.path.abspath(
        os.path.join(BASE_DIR, "..", "..", "data", "accounts.txt")
    )

    @staticmethod
    def get_allContracts(account_id):

        try: 
            with open(ContractRepository.FILE_PATH, "r") as file:

                for line in file:
                    id, contract_title, contract_text = line.strip().split(",")

                    Contract_1 = Contract(id, contract_title, contract_text)

                    if id == account_id: 
                        print(Contract_1.id + "\n" + Contract_1.contract_title + "\n" + Contract_1.contract_text)

        except FileNotFoundError:
            print("File not found")
    
    def create_newContract(account_id):




    def delete_allContracts(account_id, contract_title, contract_text):

        