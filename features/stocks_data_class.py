from features.data_handler_class import  StockQuotesHandlerClass
from features.data_handler_class import FinancialResultsHandlerClass

class StocksDataClass():
    def __init__(self, name:str, ticker:str) -> None:
        self.name = name
        self.ticker = ticker
        self.stockQuotesHandler = StockQuotesHandlerClass(self.ticker)
        self.financialResultsHandler = FinancialResultsHandlerClass(self.name)
        
    def load_data(self):
        self.stockQuotesHandler.load_data()
        self.financialResultsHandler.load_data()
    
    def store_data(self):  
        self.stockQuotesHandler.store_data_to_csv()
        self.financialResultsHandler.store_data_to_csv()
        
    def update_stored_data(self):
        self.stockQuotesHandler.download()
        self.financialResultsHandler.download()
        self.store_data()
