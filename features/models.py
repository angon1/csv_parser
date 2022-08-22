from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
import sqlalchemy
import sqlalchemy_utils


Base = declarative_base()

def populate_models(engine:sqlalchemy.engine.Engine):
    Base.metadata.create_all(engine)

class StockModelClass(Base):
    __tablename__ = 'stocks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ticker = Column(String)
    # stockQuotesHandler = StockQuotesHandlerClass(self.ticker)
    # financialResultsHandler = FinancialResultsHandlerClass(self.name)
    stock_quotas = relationship("StockQuotesModelClass", back_populates="stocks", cascade='all, delete-orphan')
    
    def __repr__(self) -> str:
        return f"stock (name={self.name}, ticker={self.ticker})"
    
    
class StockQuotesModelClass(Base):
    __tablename__ = "stockquotes"

    id = Column(Integer, primary_key=True)
    path_to_file = Column(String)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    stocks = relationship("StockModelClass", back_populates='stock_quotas' )


    
    
    


