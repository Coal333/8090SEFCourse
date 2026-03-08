

def menu_list():

    status = False

    while status == False:
        print("\"Welcome to the HKMU Banking System\"")
        selection = input("Please select one of the options to proceed:\n1. Customer Data Management\n").strip()
    
        try:
            if selection == "1":
                cust_manage_menu_list()
                status = True


        except ValueError:
            print("Please enter a numeric value between 1 to 5")



def cust_manage_menu_list():
    try:
        id = int(input("Please enter the Customer Id: "))

        if len(id) !=8:
            raise ValueError("Id must be 8 characters long")
        
        print("\"Customer Account Menu\"")
        selection = input("Please select one of the options to proceed:\n1. Customer Information Retrieval\n").strip()

        status = False
        
        try:
            if selection == "1":
                #retrieve customer data
                status = True


        except ValueError:
            print("Please enter a numeric value between 1 to 5")

    except ValueError:
        print("Please enter the a numeric value")





if __name__ == "__main__":
    menu_list()