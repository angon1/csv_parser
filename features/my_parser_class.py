#!/usr/bin/python3

import pandas as pd
from pandas_datareader import stooq
import matplotlib.pyplot as plt

pd.options.display.float_format = '${:,.2f}'.format

class MyParserClass():

    def __init__(self) -> None:
        self._loaded_file = ''
        
    @property
    def loaded_file(self):
        return self._loaded_file
    
    @loaded_file.setter
    def loaded_file(self, value: pd.DataFrame):
        self._loaded_file = value
    
    def load_file(self, filepath):
        self._loaded_file = pd.read_csv(filepath)
        self._loaded_file.pop('<TIME>')
        self._loaded_file.pop('<PER>')
        self._loaded_file.pop('<OPENINT>')
        self._loaded_file['<DATE>'] = pd.to_datetime(self._loaded_file["<DATE>"], format='%Y%m%d')

    def show(self):
        print(self._loaded_file)
        
    def calculate_daily_change(self):
        daily_change = [0]
        prev_day_close = self.loaded_file['<CLOSE>'][0]
        for it, daily_value in enumerate(self.loaded_file['<CLOSE>']):
            if it == 0:
                continue
            daily_change.append(round(((daily_value - prev_day_close)/prev_day_close*100),2))
            prev_day_close = daily_value
            # self.loaded_file.insert(daily_change)
        self.loaded_file["<DAILY CHANGE>"] = daily_change
        
        
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
        pass
    @classmethod
    def download(self):
        erb_data = stooq.StooqDailyReader('wig20.pl')
        var = erb_data.read()
        print(var)