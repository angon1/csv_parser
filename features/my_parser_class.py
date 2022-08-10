#!/usr/bin/python3

import pandas as pd
from pandas_datareader import stooq
import matplotlib.pyplot as plt

pd.set_option('display.float_format', str)

class MyParserClass():

    def __init__(self) -> None:
        self._loaded_file = ''
        
    @property
    def loaded_file(self):
        return self._loaded_file
    
    @loaded_file.setter
    def loaded_file(self, value: pd.DataFrame):
        self.loaded_file = value
    
    def load_file(self, filepath):
        self._loaded_file = pd.read_csv(filepath)
        self._loaded_file.pop('<TIME>')
        self._loaded_file.pop('<PER>')
        self._loaded_file.pop('<OPENINT>')
        self._loaded_file['<DATE>'] = pd.to_datetime(self._loaded_file["<DATE>"], format='%Y%m%d')

    def show(self):
        print(self._loaded_file)
        
class PlotDataClass():
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def plot_on_close_date(cls, data: pd.DataFrame):
        data.plot(x='<DATE>', y='<CLOSE>')
        
        plt.savefig("dupa")
        data.to_csv("on_close.csv")
        
    @staticmethod
    def plot_low_date(data: pd.DataFrame):
        data.plot(x='<DATE>', y='<LOW>', color= 'red')
        plt.savefig("dupa")
        data.to_csv("low.csv")
        
class DownloadDataClass():
    
    def __init__(self) -> None:
        self._parsed_data = None
    
    def download(self, company_name='wig20.pl'):
        data = stooq.StooqDailyReader(company_name)
        self._parsed_data = data.read()
        # print(var)
        
    
    def get_data(self):
        return self._parsed_data