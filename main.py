#!/usr/bin/python3
import os
import matplotlib.pyplot as plt
import pandas as pd

from features import MyParserClass
from features.my_parser_class import DownloadDataClass, PlotDataClass


if __name__ == "__main__":
    
    os.environ["PYTHONPATH"] = "".join(os.getcwd())
    print(os.environ["PYTHONPATH"])

    DownloadDataClass.download()
    # path_to_filebase = "".join([os.getcwd(),'/data/erb.csv'])

    # data = MyParserClass()
    # data.load_file(path_to_filebase)

    # data.show()
    # data.show_but_static()

    # PlotDataClass.plot_low_date(data.loaded_file)
    # PlotDataClass.plot_on_close_date(data.loaded_file)
else:
    print("main imported")
