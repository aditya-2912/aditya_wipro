import pytest
@pytest.fixture
def data():
    print("Setup: creating data")
    data = [1, 2, 3, 4, 5]

    yield data   # test runs here

    print("Teardown: cleaning up")


def test_one(data):
    assert 3 in data


def test_two(data):
    assert len(data) == 5
