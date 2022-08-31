#!/usr/bin/python3    
from features.raw_data_class import RawDataClass
from features.raw_data_parser_class import RawDataParserClass
from stocks import wig20list, Stock

def run_data_gatherer():
    
    stocks = [20]
    
    for index, stock in enumerate(wig20list):
        dataHandler = RawDataClass(wig20list[index][0],wig20list[index][1])
        dataParser = RawDataParserClass()
        stock = Stock()
        
        dataHandler.load_data()
        dataParser.parse(dataHandler, stock)
        stocks.append(stock)

    for index, stock in enumerate(stocks):     
        stocks[index].print()