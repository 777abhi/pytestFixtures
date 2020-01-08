from math_func import StudentDB
import pytest

@pytest.fixture(scope='module')
def db():
    print('----------setup-------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('----------teardown-------------')
    db.close()

def test_scott_data(db):
    print('test1')
    scott_data = db.get_data('Scott')
    print('test2')
    assert scott_data['id'] ==1
    print('test3')