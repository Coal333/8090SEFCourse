from src.repositories.account_repository import AccountRepository

class CustomerInfoManager:

    def CustomerInfoEdit(selection_1, account_id):
        try:
                if selection_1 == "1":
                      input_1 = input("Please enter the new First Name: ")

                      if input_1.isalpha():
                        AccountRepository.edit_customer_data(account_id, input_1, selection_1)
                      else: print("Invalid input. Only letters are allowed.")
                      
                elif selection_1 == "2":
                      input_1 = input("Please enter the new Last Name: ")
                      if input_1.isalpha():
                        AccountRepository.edit_customer_data(account_id, input_1, selection_1)
                      else: print("Invalid input. Only letters are allowed.")
                
                elif selection_1 == "3":
                      input_1 = input("Please enter the new Current Balance: ")
                      if input_1.isdigit():
                        AccountRepository.edit_customer_data(account_id, input_1, selection_1)
                      else: print("Invalid input. Only letters are allowed.")

                elif selection_1 == "4":
                      input_1 = input("Please enter the new Checking Balance: ")
                      if input_1.isdigit():
                        AccountRepository.edit_customer_data(account_id, input_1, selection_1)
                      else: print("Invalid input. Only letters are allowed.")
                
                elif selection_1 == "5":
                      input_1 = input("Please enter the new Account Type: ")
                      if input_1.isalpha():
                        AccountRepository.edit_customer_data(account_id, input_1, selection_1)
                      else: print("Invalid input. Only letters are allowed.")
                      
        except ValueError:
                print("Please enter a numeric value between 1 to 5")