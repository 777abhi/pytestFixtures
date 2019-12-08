from mydb import MyDB

conn = None
cur = None

def setup_module(module):
    global conn
    global cur
    db = MyDB()
    conn = db.connect("server")
    cur = conn.Cursor()

def teardown_modulw(module):
    cur.close()
    conn.close()
    
def test_something():
    id = cur.execute("1")
    assert id == 123

def test_something2():
    id = cur.execute("2")
    assert id == 321