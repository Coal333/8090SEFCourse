from src.models.account import Account

#Business account class, Account is the parent
class Customer_Account(Account):

    bank_name = "HKMU BANK"

    #Constructor
    def __init__(self, id, first_name, last_name, balance_current, balance_checking, acc_type):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.balance_current = balance_current
        self.balance_checking = balance_checking
        self.acc_type = acc_type

    #method that displays full customer information
    def display_info(self):
        print(f"{self.id}, {self.last_name}")



