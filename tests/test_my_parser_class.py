import time
import pandas as pd
import pytest

from features import MyParserClass

def test_instance_creation():
    assert isinstance(MyParserClass(),MyParserClass)
    
def test_calculate_daily_change(daily_change_test_data, expected_results):
    test_parser = MyParserClass()
    test_parser.loaded_file = daily_change_test_data
    test_parser.calculate_daily_change()
    assert test_parser.loaded_file["<DAILY CHANGE>"].tolist() == expected_results
    
def test_one(return_one):
    assert return_one == 1

@pytest.mark.parametrize("input, expected", [("time_now","time_now"),(2,2)], indirect=["input", "expected"])    
def test_some(input, expected):
    assert input == expected
    
# def test_time_now(time_now):
#     print (time_now)
    
# def test_time_in_5_sec(time_now):
#     time.sleep(5)
#     print(time_now)