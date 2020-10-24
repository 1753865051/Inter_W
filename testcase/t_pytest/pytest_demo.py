import pytest
def func(x):
    return x+1

def test_a():
    print("testA")
    assert func(3)==5
def test_b():
    print("testB")
    assert 1

if __name__ == '__main__':
    pytest.main(["pytest_demo.py"])