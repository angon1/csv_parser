#!/usr/bin/python3
import os
# import uvicorn

from data_gatherer_run import run_data_gatherer

if __name__ == "__main__":   
    os.environ["PYTHONPATH"] = "".join(os.getcwd())
    print(os.environ["PYTHONPATH"])
    
    # uvicorn.run("features.presenation:app",port=8000) 
    run_data_gatherer()

else:
    print("main imported")