import os
import sqlalchemy
import sqlalchemy_utils

from features import models


def create_db_connection(name:str = 'my_db.db'):
    db_path = os.getenv('PYTHONPATH')
    # db = "sqlite://"+db_path+"/"+name
    db = "sqlite:///"+db_path+"/"+name
    print(db)
    engine = sqlalchemy.create_engine(db, echo=True, future=True)
    return engine

def create_db(engine:sqlalchemy.engine.Engine):
    if not sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.create_database(engine.url)
    else:
        pass
    
    
def start_session(engine:sqlalchemy.engine.Engine):
    Session=sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    return session
    
    
# def connect_to_db(db_name:str = 'my_db.db'):
#     engine = create_db_connection(db_name)
#     create_db(engine)

def start_db(db_name:str = 'my_db.db'):
    engine = create_db_connection(db_name)
    create_db(engine)
    models.populate_models(engine)
    return start_session(engine)

# start_db()
    

def select_them_all(sesion):
    pass