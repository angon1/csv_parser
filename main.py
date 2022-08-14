#!/usr/bin/python3
import os
# import uvicorn

if __name__ == "__main__":   
    os.environ["PYTHONPATH"] = "".join(os.getcwd())
    print(os.environ["PYTHONPATH"])
    
    # uvicorn.run("features.presenation:app",port=8000)  
    
    
else:
    print("main imported")
