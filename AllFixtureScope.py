import pytest

@pytest.fixture(scope='session')
def fixture_sess():
    print("Inside session fixture")

@pytest.fixture(scope='function')
def fixture_func():
    print("Inside function fixture")

@pytest.fixture(scope='module')
def fixture_modl():
    print("Inside module fixture")

@pytest.fixture(scope='class')
def fixture_clss():
    print("Inside class fixture")

class TestOrder:
    @pytest.mark.usefixtures('fixture_sess', 'fixture_modl', 'fixture_clss', 'fixture_func')
    def test_one(self):
      print("Inside test")