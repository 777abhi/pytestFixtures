import pytest

@pytest.mark.parametrize("val,out", [
(3, 27),
(4, 15),
(5, 125)
])
def test_cube_it(val, out):
    print('val^3: '+str(val*val*val))
    assert val*val*val == out

#python3 -m -v pytest -s --tb=no test.py