from hasher import hash_url

def test_hashing():
    url = "http://domain.com/"
    assert hash_url(url) == '0f4366de78756f34670f5bc4969f84d3'
