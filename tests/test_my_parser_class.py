from features import MyParserClass


def test_instance_creation():
    assert isinstance(MyParserClass(),MyParserClass)
    
def test_is_header_loaded():
    test_parser = MyParserClass()
    pass