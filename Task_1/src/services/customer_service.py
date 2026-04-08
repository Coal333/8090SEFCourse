from src.repositories.account_repository import AccountRepository

class CustomerService:

    def check_accountInfo(self, account_id):
        return AccountRepository.check_customer_id(account_id)

    def get_accountInfo(self, account_id):
        AccountRepository.load_customer_data(account_id)

    def transfer_money(self, account_id):

        Customer_Service = CustomerService()

        ID_False = False

        while ID_False == False:
            while True:
                send_to_id = input("Please enter the Account ID you would like to transfer the money to: ").strip()

                if len(send_to_id) != 8:
                    print("Invalid ID. Must be 8 characters.")
                else:
                    break
            
            #Check if the ID exists
            status = Customer_Service.check_accountInfo(send_to_id)
            ID_False = status

            if status == False:
                print("The inputted ID does not exist in the records")
            else:
                print("The inputted ID exists in the records")

        try:

            choice = input("To transfer to the Recipient's current account enter 1\n" \
            "To transfer to the Recipient's checking account enter 2\n"
            "Note: The Sender's same type of banking account will be used to transfer the money: ")
                
            try:

                amount = float(input("Please insert the amount you want to transfer: "))

                if amount <= 0:
                    print("Value must be greater than 0")
            
            except ValueError:
                print("Please enter a numeric value")

            AccountRepository.transfer_money(account_id, send_to_id, choice, amount)

        except ValueError:
                print("Please enter a numeric value")
