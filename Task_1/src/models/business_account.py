from src.models.account import Account

class Business_Account(Account):

    def __init__(self, id, company_name, company_type, balance_current, balance_checking, acc_type):
        super().__init__(id)
        self.company_name = company_name
        self.company_type =  company_type
        self.balance_current = balance_current
        self.balance_checking = balance_checking
        self.acc_type = acc_type

    def display_info(self):
        print(f"{self.id}, {self.company_name}")



