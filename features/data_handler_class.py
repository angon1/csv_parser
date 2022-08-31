#!/usr/bin/python3

import os
import pandas as pd
import pandas_datareader.data as pd_dr        

class DataHandlerClass():
    
    def __init__(self) -> None:
        self.data = pd.DataFrame()
        self.path_to_file = ""

    def download(self):
        print('use only in derivative')
        
    def print_data(self): 
        print(self.data)

    def store_data_to_csv(self):
        self.data.to_csv(self.path_to_file)
        
    def load_data_from_csv(self):
        self.data = pd.read_csv(self.path_to_file)
        
    def load_data(self):
        if os.path.exists(self.path_to_file):
            self.load_data_from_csv()
        else:
            self.download()
            self.store_data_to_csv()
            
    def file_exist(self):
        if os.path.exists(self.path_to_file):
            return True
        else:
            return False
            
class FinancialResultsHandlerClass(DataHandlerClass):
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.path_to_file = ""+os.getcwd()+'/raw_data/financial_results/'+self.name+'.csv'
    
    def download(self):
        try:
            self.data = pd.read_html('https://www.bankier.pl/gielda/notowania/akcje/'+self.name+'/wyniki-finansowe')[0]
        except:
            print('error')
            self.data = pd.DataFrame()
        
class StockQuotesHandlerClass(DataHandlerClass):
    
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker
        self.path_to_file = "".join([os.getcwd(),'/raw_data/stock_quotes/' + self.ticker + '.csv'])
        
    def download(self):
        try:
            self.data = pd_dr.DataReader(self.ticker+'.pl', 'stooq')
        except:
            print('error')
            self.data = pd.DataFrame()