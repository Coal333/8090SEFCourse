from src.repositories.account_repository import AccountRepository
from src.models.account import Account

class CustomerService:

    def get_accountInfo(self, account_id):
        return AccountRepository.load_data()