#Create a function named create_student() as a factory as fixture. 
#This fixture will receive a string, 
#and must return a function that returns a dictionary with name as the value for the "name" key, 
#and 'A' as the value for the "grade" key.

#Create a test function named test_one(),
#where you use the fixture function twice with arguments "Ravi" and "Abdul"


import pytest

@pytest.fixture
def create_student():
    def _make_record(name):
        return {
            "name": name,
            "grade" : 'A'
        }
    return _make_record

def test_one(create_student):
    o1 = create_student("Ravi")
    o2 = create_student("Abdul")
    print(o1)
    print(o2)