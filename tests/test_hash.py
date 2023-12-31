from utils.hasher import hash_url

def test_hashing():
    # The test verifies that the 'hash_url' function correctly hashes the given URL.
    url = "http://domain.com/"
    expected_hash = '0f4366de78756f34670f5bc4969f84d3'
    assert hash_url(url) == expected_hash
