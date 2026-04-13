
class Contract:

    def __init__(self, id, company_name, contract_title, contract_text):
        self.id = id
        self.company_name = company_name
        self.contract_title = contract_title
        self.contract_text = contract_text

    def get_contract_title(self):
        return self.contract_title

    def set_contract_title(self, contract_title):
        self.contract_title = contract_title