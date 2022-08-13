#!/usr/bin/python3
import os
# import uvicorn

from features.stock_data_parser_class import StockDataParserClass
from features.data_handler_class import  DataHandlerClass
from features.plot_data_class import PlotDataClass

class Stocks():
        def __init__(self, _name, _ticker) -> None:
            self.name = _name
            self.ticker = _ticker
            self.dataHandler = DataHandlerClass()
            self.dataHandler.download(self.ticker)
            StockDataParserClass.calculate_daily_change(self.dataHandler.data)
            self.dataHandler.store_data_to_csv()

if __name__ == "__main__":   
    os.environ["PYTHONPATH"] = "".join(os.getcwd())
    print(os.environ["PYTHONPATH"])
    
    # uvicorn.run("features.presenation:app",port=8000)  
    


    wig20 = []
    
    wig20.append(Stocks('Allegro', 'ale'))
    wig20.append(Stocks('Asseco Poland', 'acp'))
    wig20.append(Stocks('CCC', 'ccc'))
    wig20.append(Stocks('CD Projekt', 'cdr'))
    wig20.append(Stocks('Cyfrowy Polsat', 'cps'))
    wig20.append(Stocks('Dino', 'dnp'))
    wig20.append(Stocks('Jastrzebska Spolka Weglowa', 'jsw'))
    wig20.append(Stocks('Kety', 'kty'))
    wig20.append(Stocks('KGHM', 'kgh'))
    wig20.append(Stocks('LPP', 'lpp'))
    wig20.append(Stocks('Mbank', 'mbk'))
    wig20.append(Stocks('Orange pl', 'opl'))
    wig20.append(Stocks('PEKAO', 'peo'))
    wig20.append(Stocks('Pepco', 'pco'))
    wig20.append(Stocks('PGE', 'pge'))
    wig20.append(Stocks('PGNiG', 'pgn'))    
    wig20.append(Stocks('PKNOrlen', 'pkn'))
    wig20.append(Stocks('PKO BP', 'pko'))
    wig20.append(Stocks('PZU', 'pzu'))
    wig20.append(Stocks('Santander pl', 'spl'))
    
    wig20index = Stocks('Wig20', 'wig20')
    
    for st in wig20:
        print(st.name)

    #PlotDataClass.plot_on_close_date(wig20.data)
else:
    print("main imported")
