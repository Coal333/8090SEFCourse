from src.repositories.contract_repository import ContractRepository

class BusinessService:

    def check_accountInfo(self, account_id):
        ContractRepository.get_allContracts(account_id)

    def get_accountInfo(self, account_id):

        while True:
            contract_title = input("Please enter the Contract Title: ").strip()

            if len(contract_title) <= 10:
                print("The contract title must be at least 10 characters")
                continue
            else:
                break

        while True:
            contract_text = input("Please enter the Contract Title: ").strip()

            if len(contract_text) == 0:
                print("The contract body has no characters")
                continue
            else:
                break

        ContractRepository.create_newContract(account_id, contract_title, contract_text)

    def get_accountInfo(self, account_id):
        ContractRepository.delete_allContracts(account_id)