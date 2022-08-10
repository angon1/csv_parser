import pytest
import pandas as pd
from datetime import datetime

@pytest.fixture
def return_one():
    return 1

@pytest.fixture()
def daily_change_test_data():
    return pd.DataFrame({"<CLOSE>": [1,2]})

@pytest.fixture(scope="function")
def time_now():
    x=datetime.now()
    return x

@pytest.fixture()
def daily_change_test_data2(data = [1,2]):
    return pd.DataFrame({"<CLOSE>": data})

@pytest.fixture()
def expected_results():
    return [0,100]