#!/usr/bin/python3

from features.raw_data_class import RawDataClass
from stocks import Stock

class RawDataParserClass():

    def __init__(self) -> None:
        pass
    
    def parseFinancialData(self, input: str):
        return int(input.replace('\xa0','').replace(',',''))
        
    def parse(self, input:RawDataClass, output:Stock):
       
        output.name['name'] = input.name
        output.name['ticker'] = input.ticker
        output.date = input.stockQuotesHandler.data['Date'][0]
        output.quotes['open'] = input.stockQuotesHandler.data['Open'][0].astype(float)
        output.quotes['high'] = input.stockQuotesHandler.data['High'][0].astype(float)
        output.quotes['low'] = input.stockQuotesHandler.data['Low'][0].astype(float)
        output.quotes['close'] = input.stockQuotesHandler.data['Close'][0].astype(float)
        output.quotes['volume'] = input.stockQuotesHandler.data['Volume'][0].astype(int)
        #output.quotes['daily change'] = input.stockQuotesHandler.data['Daily Change][0]
    
        output.results['przychody netto'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[1,5])*1000
        output.results['zysk operacyjny'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[2,5])*1000
        output.results['zysk brutto'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[3,5])*1000
        output.results['zysk netto'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[4,5])*1000
        output.results['amortyzacja'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[5,5])*1000
        output.results['ebitda'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[6,5])*1000
        output.results['aktywa'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[7,5])*1000
        output.results['kapital'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[8,5])*1000
        output.results['liczba akcji'] = self.parseFinancialData(input.financialResultsHandler.data.iloc[9,5])
        output.results['zysk na akcje'] = input.financialResultsHandler.data.iloc[10,5]
        # output.results['wartosc akcji':] = input.financialResultsHandler.data.iloc[11,5]

        try:
            output.indicators['P/E'] = output.quotes['close']*output.results['liczba akcji']/output.results['zysk netto']
            output.indicators['P/EBID'] = output.quotes['close']*output.results['liczba akcji']/output.results['zysk operacyjny']
            output.indicators['ROE'] = output.results['zysk netto']/output.results['kapital']*100
            output.indicators['ROA'] = output.results['zysk netto']/output.results['aktywa']*100
            output.indicators['ROS'] = output.results['zysk operacyjny']/output.results['przychody netto']*100
        except:
            print('error')
            output.indicators['P/E'] = 0
            output.indicators['P/EBID'] = 0
            output.indicators['ROE'] = 0
            output.indicators['ROA'] = 0
            output.indicators['ROS'] = 0

    def calculate_daily_change(data):
        data['Daily Change'] = data['Close'].diff()/data['Close'].shift(1)*100 