### Scraper needs to be integrated once professional subscription is 
### purchased
import pandas as pd

class Octoparse:

    def __init__(self, csv_file) -> None:
        self.csv_file = csv_file
    
    def __readFile__(self):
        csv_data = pd.read_csv(self.csv_file)
        csv_array = csv_data.values
        company_list = []
        for row in csv_array:
            company_list.append(row[5])
        return company_list
        
    
##'./csvfiles/Job listing by search_Indeed.csv'

# demo_obj = Octoparse("./csvfiles/Job listing by search_Indeed.csv")
# list = demo_obj.__readFile__()
