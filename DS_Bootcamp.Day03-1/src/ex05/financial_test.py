from financial import parse
import pytest


def test_total():
    result = parse('MSFT', 'Total Revenue')
    assert result[0] == 'MSFT'
    assert result[1] == 'Total Revenue'

def test_tuple():
    result = parse('MSFT', 'Total Revenue')
    assert type(result) is tuple

def test_exception():
    with pytest.raises(Exception):
        parse('lala', 'Total Revenue')

    
def test_exception_2():
    with pytest.raises(Exception):
        parse('MSFT', '')
    
def test_exception_3():
    with pytest.raises(Exception):
        parse()

if __name__ == '__main__':

    test_total()
    test_tuple()
    test_exception()
    test_exception_2()
    test_exception_3()

# pytest financial_test.py