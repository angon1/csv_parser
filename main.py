#!/usr/bin/python3
import os
# import matplotlib.pyplot as plt
# import pandas as pd
import uvicorn


# from features import MyParserClass
# from features.my_parser_class import DownloadDataClass, PlotDataClass


if __name__ == "__main__":
    
    os.environ["PYTHONPATH"] = "".join(os.getcwd())
    print(os.environ["PYTHONPATH"])
    uvicorn.run("features.presenation:app",port=8000)
    # DownloadDataClass.download()
    
    # path_to_filebase = "".join([os.getcwd(),'/data/erb.csv'])

    # data = MyParserClass()
    # data.load_file(path_to_filebase)
    # data.calculate_daily_change()
    # data.show()
    # data.show_but_static()

    # PlotDataClass.plot_low_date(data.loaded_file)
    # PlotDataClass.plot_on_close_date(data.loaded_file)
else:
    print("main imported")
