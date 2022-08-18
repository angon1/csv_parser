import pytest
from features.data_handler_class import FinancialResultsHandlerClass
import features

# def test_true(my_tru_fixture):
#     assert True == my_tru_fixture

# @pytest.mark.parametrize('value', [True, False])
# def test_true(value):
#     assert True == value
    
# @pytest.mark.parametrize('value, expected', [(True,True), (False,True)])
# def test_123(value, expected):
#     assert expected == value
    
# @pytest.mark.xfail(reason = 'will refactor later')
# def test_fail():
#     assert False
    
# @pytest.mark.skip(reason= 'lazy test')
# def test_lazy():
#     assert False
    
# def test_FinancialDataHandler_1():
#     dataHandler = FinancialResultsHandlerClass('str')
#     assert dataHandler

def test_FinancialDataHandler_download(mocker):
    mocker.patch('features.data_handler_class.pd.read_html', return_value = '123')
    dataHandler = FinancialResultsHandlerClass('str')
    dataHandler.download()
    dataHandler.download()
    features.data_handler_class.pd.read_html.assert_called_once()
    print(dataHandler.data)
    assert dataHandler