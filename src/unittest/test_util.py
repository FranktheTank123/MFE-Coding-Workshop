from src.unittest.util import add, divide2

def test_add():
	assert 3 == add(1,2)

def test_divide2():
	assert 2.5 == divide2(5,2)