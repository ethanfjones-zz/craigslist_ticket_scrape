import pandas as pd 

def cleanup():
    tickets = pd.read_csv(r'f:\webscrap\craigslist\craigslist\results.csv')

    tickets = tickets.dropna()
    pd.options.mode.chained_assignment = None 
    tickets['Price'] = tickets['Price'].map(lambda x: x.lstrip('$'))
    tickets = tickets[tickets['Price'] != '1']
    return tickets 