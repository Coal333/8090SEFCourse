import os
from src.models.contract import Contract

#Contract Repository Class that manages contract data (Storing and Retrieving data)
class ContractRepository:

    BASE_DIR = os.path.dirname(__file__)

    FILE_PATH = os.path.abspath(
        os.path.join(BASE_DIR, "..", "..", "data", "contracts.txt")
    )

    @staticmethod
    #Gets all the contracts of the account
    def get_allContracts(account_id):

        try: 
            with open(ContractRepository.FILE_PATH, "r") as file:

                for line in file:
                    id, company_name, contract_title, contract_text = line.strip().split(",")

                    Contract_1 = Contract(id, company_name, contract_title, contract_text)

                    #Makes sure the account contracts are only printed
                    if id == account_id: 
                        print(Contract_1.id + "\n" + Contract_1.company_name + "\n" + Contract_1.contract_title + "\n" + Contract_1.contract_text + "\n")

        except FileNotFoundError:
            print("File not found")
    
    #Creates a new contract under the account
    def create_newContract(id_1, company_name, contract_title, contract_text):

        try: 
            with open(ContractRepository.FILE_PATH, "a+") as file:

                #Goes to the end of the file
                file.seek(0, 2)

                if file.tell() != 0:
                    file.seek(file.tell() - 1)
                    if file.read(1) != "\n":
                        file.write("\n")

                file.write(f"{id_1},{company_name},{contract_title},{contract_text}\n")

        except FileNotFoundError:
            print("File not found")

    #Deletes all contracts of the account
    def delete_allContracts(account_id):

        try:
            with open(ContractRepository.FILE_PATH, "r") as file:
                lines = file.readlines()

            updated_lines = []

            for line in lines:
                id, company_name, contract_title, contract_text = line.strip().split(",", 3)

                #If the contract is not the account's it is added to the list to be kept
                if id != account_id:
                    updated_lines.append(line)
                
            with open(ContractRepository.FILE_PATH, "w") as file:
                file.writelines(updated_lines)

        except FileNotFoundError:
            print("File not found")

        