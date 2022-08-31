    #!/usr/bin/python3
    #     if type(param)==str:
    #         print('hurra!\o/')
    #     else:
    #         raise(TypeError)
    # try:
    #     asdf('1')
    # except TypeError as er:
    #     print('not very smart, are you?')
    #     print(er.with_traceback)
    # except:
    #     print('str you morron!')
    # finally:
    #     print('the end')
    # a = None
#     # print(a)
    
# def asdf(a,b):
#     '''
#     qwer
#     >>> asdf(1,2)
#     3
#     '''
#     return a+b





from curses import echo
from enum import unique
import sqlalchemy
from sqlalchemy import orm
import sqlalchemy_utils

wig20list = [
    ('ALLEGRO', 'ale'),
    ('ASSECOPOL', 'acp'),
    ('CCC', 'ccc'),
    ('CDPROJEKT', 'cdr'),
    ('CYFRPLSAT', 'cps'),
    ('DINOPL', 'dnp'),
    ('JSW', 'jsw'),
    ('KETY', 'kty'),
    ('KGHM', 'kgh'),
    ('LPP', 'lpp'),
    ('MBANK', 'mbk'),
    ('ORANGEPL', 'opl'),
    ('PEKAO', 'peo'),
    ('PEPCO', 'pco'),
    ('PGE', 'pge'),
    ('PGNIG', 'pgn'),
    ('PKNORLEN', 'pkn'),
    ('PKOBP', 'pko'),
    ('PZU', 'pzu'),
    ('SANPL', 'spl')
    ]

engine = sqlalchemy.create_engine('sqlite:///baza.db', echo=True, future=True)
sqlalchemy_utils.create_database(engine.url)
Session = orm.sessionmaker(bind=engine)
Base = orm.declarative_base()

class myModelClass(Base):
    __tablename__ = 'stocks'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    my_other_model_class = orm.relationship("myOtherModelClass", back_populates="stocks_rel", cascade='all, delete-orphan')
    
    def append_to(self, indicators):
        if type(indicators) == list:
            self.my_other_model_class.extend(indicators)
        else:
            self.my_other_model_class.append(indicators)
            
    def add_indicators(self, *args):
        self.my_other_model_class.extend(args)
        
    @classmethod
    def select_stock(cls, name, session):
        return session.query(cls).filter_by(name=name).first()
    
    
class myOtherModelClass(Base):
    __tablename__ = 'indicators'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    stocks_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('stocks.id'))
    
    stocks_rel = orm.relationship("myModelClass", back_populates='my_other_model_class')
   
Base.metadata.create_all(engine)

indicator_model = myOtherModelClass(name='price')
# stock_model = myModelClass(name='wig30')
# stock_model.my_other_model_class.append(indicator_model)

# stocks_db_list = list()
indicator2 = myOtherModelClass(name='value')
# stock_model.my_other_model_class.append(indicator2)
# for el in wig20list:
#     stocks_db_list.append(myModelClass(
#             name=(el[0]), 
#             my_other_model_class = [myOtherModelClass(name=el[1])]
#             ))

session = Session()
# session.add(stock_model)
# session.commit()

# req = session.query(myModelClass).where(sqlalchemy.Column('name')=='wig20').one()

# req = session.query(myModelClass).filter_by(name='wig30').one()

indicator3 = myOtherModelClass(name='volume')
indicator4 = myOtherModelClass(name='daily_change')
inds = [indicator_model, indicator2, indicator3]
# req.add_indicators(indicator3,indicator4)

stock_model = myModelClass(name='swig80')
stock_model.append_to(inds)
stock_model.append_to(indicator4)

session.add(stock_model)
session.commit()

swig80 = myModelClass.select_stock('swig80', session)
print('dupa')
print(swig80)