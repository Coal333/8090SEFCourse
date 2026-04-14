from src.models.account import Account

class Customer_Account(Account):

    def __init__(self, id, first_name, last_name, balance_current, balance_checking, acc_type):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.balance_current = balance_current
        self.balance_checking = balance_checking
        self.acc_type = acc_type

    def display_info(self):
        print(f"{self.id}, {self.last_name}")



