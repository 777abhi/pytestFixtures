from mydb import MyDB

import pytest

@pytest.fixture(scope="module")
def cur():
    print("setting up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.Cursor()
    yield curs
    curs.close()
    conn.close()
    print("closing")

def test_something(cur):
    id = cur.execute("1")
    assert id == 123

def test_something2(cur):
    id = cur.execute("2")
    assert id == 321