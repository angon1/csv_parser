#!/usr/bin/python3
import os
from fastapi import FastAPI, Response
import pandas
import sqlite3
import sqlalchemy
import sqlalchemy_utils

from features import DownloadDataClass
# from fastapi.templating import Jinja2Templates
# templates = Jinja2Templates(directory="webapp")

app = FastAPI()
engine = sqlalchemy.create_engine('sqlite:///wig20.db')


def config():
    os.environ["PYTHONPATH"] = "".join(os.getcwd())
    
    print(os.environ["PYTHONPATH"])

@app.get("/")
def root():
    return "Hello"

@app.get("/erb")
def get_erb_data():
    erb_data = DownloadDataClass()
    erb_data.download('erb.pl')
    return erb_data.get_data()

@app.get("/wig20")
def get_erb_data():
    data = DownloadDataClass()
    data.download('wig20.pl')
    data = data.get_data()
    # data.style.format("{:.1f}")
    # print(data.to_html())
    return Response(data.to_html(justify='justify-all') )
    # return data.to_html()

def create_wig20_table():
    data = DownloadDataClass()
    data.download('wig20.pl')
    data = data.get_data()
    data.to_sql('wig20pl',con=engine, if_exists='append')

@app.get("/wig20db")
def get_wig20_table():
    data = pandas.read_sql('SELECT * FROM wig20pl',engine)
    return Response(data.to_html(justify='justify-all') )
    # data.download('wig20.pl')
    # data = data.get_data()
    # data.to_sql("wig20pl",engine)
    
def add_daily_change(data: pandas.DataFrame = None):
    data = data if data else DownloadDataClass()
    data.download('wig20.pl')
    data = data.get_data()
    data['daily'] = data['Close'].diff()/data['Close'].shift(1)*100
    print(data)

if __name__ == "__main__":
    config()
    
    if not sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.create_database(engine.url)
    # Connect the database if exists.
    conn = engine.connect.execution_options(autocommit=True)
    create_wig20_table()
    add_daily_change()

else:
    config()
    # engine = sqlalchemy.create_engine('sqlite:///wig20.db')
    if not sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.create_database(engine.url)
    else:
        # Connect the database if exists.
        engine.connect()
    create_wig20_table()
    add_daily_change()