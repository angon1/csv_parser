#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

class PlotDataClass():
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def plot_on_close_date(cls, data: pd.DataFrame):
        data.plot(x='Date', y='Close')
        
        plt.savefig("dupa")
        data.to_csv("on_close.csv")