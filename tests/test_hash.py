import os

def test_hashing():
    url = "http://domain.com/"
    assert hash(url) == -345501838550440081

def test_seed_value():
    assert os.environ['PYTHONHASHSEED'] == '0'
