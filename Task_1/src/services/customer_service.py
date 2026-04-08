from src.repositories.account_repository import AccountRepository
from src.services.customer_service import CustomerService

Customer_service = CustomerService()

class CustomerService:

    def check_accountInfo(self, account_id):
        return AccountRepository.check_customer_id(account_id)

    def get_accountInfo(self, account_id):
        AccountRepository.load_customer_data(account_id)

    def transfer_money(self, account_id):

        while(ID_False == False):
            while True:
                send_to_id = input("Please enter the Account ID you would like to transfer the money to: ").strip()

                if len(send_to_id) != 8:
                    print("Invalid ID. Must be 8 characters.")
                else:
                    break
            
            #Check if the ID exists
            status = Customer_service.check_accountInfo(id)
            ID_False = status

            if status == False:
                print("The inputted ID does not exist in the records")
            else:
                print("The inputted ID exists in the records")

        while True:
            choice = input("To transfer to the current account enter 1\n" \
            "To transfer to the checking account enter 2: ")

            if choice == 1 or choice == 2:
                break
            else:
                continue
                
        while True:
            try:

                amount = input("Please insert the amount you want to transfer: ")

                if amount <= 0:
                    print("Value must be greater than 0")
                    continue

                break
            
            except ValueError:
                print("Please enter a numeric value")

        AccountRepository.transfer_money(account_id, send_to_id, choice, amount)
