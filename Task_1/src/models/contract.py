
#Contract CLass
class Contract:

    #Constructor
    def __init__(self, id, company_name, contract_title, contract_text):
        self.id = id
        self.company_name = company_name
        self.contract_title = contract_title
        self.contract_text = contract_text

    #method that gets the contract title
    def get_contract_title(self):
        return self.contract_title


    #method that sets the contract title
    def set_contract_title(self, contract_title):
        self.contract_title = contract_title