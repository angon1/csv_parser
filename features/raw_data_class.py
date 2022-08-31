from features.data_handler_class import  StockQuotesHandlerClass
from features.data_handler_class import FinancialResultsHandlerClass

class RawDataClass():
    def __init__(self, name:str, ticker:str) -> None:
        self.name = name
        self.ticker = ticker
        self.stockQuotesHandler = StockQuotesHandlerClass(self.ticker)
        self.financialResultsHandler = FinancialResultsHandlerClass(self.name)
        
    def load_data_from_csv(self):
        self.stockQuotesHandler.load_data_from_csv()
        self.financialResultsHandler.load_data_from_csv()
    
    def store_data_to_csv(self):  
        self.stockQuotesHandler.store_data_to_csv()
        self.financialResultsHandler.store_data_to_csv()
        
    def download(self):
        self.stockQuotesHandler.download()
        self.financialResultsHandler.download()
        self.store_data_to_csv()

    def load_data(self):
        if not self.stockQuotesHandler.file_exist():
            self.stockQuotesHandler.download()
            self.stockQuotesHandler.store_data_to_csv()
        if not self.financialResultsHandler.file_exist():
            self.financialResultsHandler.download()
            self.financialResultsHandler.store_data_to_csv()
        self.load_data_from_csv()