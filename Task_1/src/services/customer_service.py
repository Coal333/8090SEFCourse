from src.repositories.account_repository import AccountRepository
from src.models.account import Account

class CustomerService:

    def get_accountInfo(self, account_id):
        AccountRepository.load_customer_data(account_id)