import pytest
@pytest.fixture

def data():
    return [1,2,3,4,5]

def test_one(data):
    assert 3 in data
    print(data)

def test_two(data):
    assert len(data) == 5
    print(len(data))


