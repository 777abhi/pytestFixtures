#run 1 test - pytest Options.py::test_add -v
#run specific test - pytest Options.py -v -k "add"
#run specific test - pytest Options.py -v -k "add or string"
#run specific test - pytest Options.py -v -k "add and string"
#run with tag - pytest Options.py -v -m number
#exit on 1st failure - pytest Options.py -v -x
#exit on 1st failure with no stack trace - pytest Options.py -v -x --tb=no
#exit on x failure with no stack trace - pytest Options.py -v -x --maxfail=x
#skip reason show - pytest Options.py -v -rsx
#execute print statement in test - pytest Options.py -v -s
#execute print statement in test - pytest Options.py -v --capture=no
#less information - pytest Options.py -v -q

import pytest 
import sys

def add(x,y=2):
    return x + y
def product(x,y=2):
    return x * y

@pytest.mark.skip(reason="do not run test add")
def test_add():
    assert add(7,3) == 10
    assert add(7) == 9
    print('----------------------')

@pytest.mark.number
def test_product():
    assert product(5,5) == 25
    assert product(5) ==10

@pytest.mark.skipif(sys.version_info <(3,3), reason="do not run test if py version is greater than 3.3")
def test_add_strings():
    result = add('Hello',' World!!')
    assert result == 'Hello World!!'
    assert type(result) is str
    assert 'Hello' in result
    print('----------------------')

@pytest.mark.strings
def test_product_strings():
    result = product('Hello ',3)
    assert result == 'Hello Hello Hello '
    assert type(result) is str
    assert 'Hello' in result