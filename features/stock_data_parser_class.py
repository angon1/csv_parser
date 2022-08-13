#!/usr/bin/python3

import pandas as pd

pd.options.display.float_format = '${:,.2f}'.format

class StockDataParserClass():

    def __init__(self) -> None:
        pass
     
   
    def calculate_daily_change(data):
        data['Daily Change'] = data['Close'].diff()/data['Close'].shift(1)*100