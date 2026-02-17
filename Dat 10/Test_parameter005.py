import pytest

@pytest.mark.parametrize("a,b,res",[(1,2,3),(4,5,9)])
def test_add(a,b,res):
    print(a+b)
    assert a+b == res

@pytest.mark.smoke
def test_smoke():
    assert True

@pytest.mark.skip
def test_skip():
    pass