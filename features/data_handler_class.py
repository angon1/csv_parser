#!/usr/bin/python3

import os
import pandas as pd
import pandas_datareader.data as pd_dr        

class DataHandlerClass():
    
    def __init__(self) -> None:
        data = pd.DataFrame
        stock = ''
        path_to_file = ''
        
    @property
    def data(self):
        return self.data
        
    @classmethod
    def download(self, stock):
        self.stock = stock
        self.path_to_file = "".join([os.getcwd(),'/data/' + self.stock + '.csv'])
        self.data = pd_dr.DataReader(stock+'.pl', 'stooq')
        
    @classmethod
    def print_data(self): 
        print(self.data)

    @classmethod
    def store_data_to_csv(self):
        self.data.to_csv(self.path_to_file)