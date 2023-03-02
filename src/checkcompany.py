
class CompanyValidity:

    def __init__(self, company_list):
        self.company_list = company_list
    
    def removeInvalidCompanies(self):
        for company in self.company_list:
            value = company.find("Staffing")
            if(value != -1):
                self.company_list.remove(company)
        return self.company_list
