#!/usr/bin/python3
import os
from fastapi import FastAPI, Response
import pandas
from features import DownloadDataClass
# from fastapi.templating import Jinja2Templates
# templates = Jinja2Templates(directory="webapp")

app = FastAPI()

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
    data.download('erb.pl')
    data = data.get_data()
    # data.style.format("{:.1f}")
    print(data.to_html())
    return Response(data.to_html(justify='justify-all') )
    # return data.to_html()


if __name__ == "__main__":
    config()
    
    
    
    

else:
    print("main imported")
