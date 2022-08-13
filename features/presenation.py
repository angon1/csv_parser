from typing import Union
from features.my_parser_class import MyParserClass
import sqlalchemy
import sqlalchemy_utils
import pandas

from fastapi import FastAPI
from fastapi import Response

app = FastAPI()
db = sqlalchemy.create_engine('sqlite:///wig20.db')

# def config_app():
#     app.add_middleware(DBSessionMiddleware, db_url="sqlite://")
#     return app

# app = config_app()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/wig20")
def present_wig20():
    wig20 = MyParserClass()
    wig20.load_file("../data/erb.csv")
    wig20.calculate_daily_change()
    return Response(wig20.loaded_file.to_html())

@app.get("/wig20db")
def wig20_db():
    if not sqlalchemy_utils.database_exists(db.url):
        sqlalchemy_utils.create_database(db.url)
    db.connect()
    wig20 = MyParserClass()
    wig20.load_file("../data/erb.csv")
    wig20.calculate_daily_change()
    wig20.loaded_file.to_sql("wig20",con=db, if_exists="append")
    data = pandas.read_sql('SELECT * FROM wig20',db)
    return Response(data.to_html(justify='justify-all') )