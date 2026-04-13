from src.repositories.contract_repository import ContractRepository

class BusinessService:

    def get_allContracts(self, account_id):
        ContractRepository.get_allContracts(account_id)

    def create_newContract(self, account_id):

        while True:
            company_name = input("Please enter the Company name: ").strip()

            if len(company_name) == 0:
                print("The company name has no characters")
                continue
            else:
                break

        while True:
            contract_title = input("Please enter the Contract Title: ").strip()

            if len(contract_title) <= 10:
                print("The contract title must have at least 10 characters")
                continue
            else:
                break

        while True:
            contract_text = input("Please enter the Contract Body: ").strip()

            if len(contract_text) == 0:
                print("The contract body has no characters")
                continue
            else:
                break

        ContractRepository.create_newContract(account_id, company_name, contract_title, contract_text)

    def delete_allContracts(self, account_id):
        ContractRepository.delete_allContracts(account_id)