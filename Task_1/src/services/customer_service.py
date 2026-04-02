from src.repositories.account_repository import AccountRepository

class CustomerService:

    def check_accountInfo(self, account_id):
        return AccountRepository.check_customer_id(account_id)

    def get_accountInfo(self, account_id):
        AccountRepository.load_customer_data(account_id)