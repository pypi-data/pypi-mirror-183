import urllib.request


def test_needs_internet(needs_internet):
    """
    This test should always succeed or be skipped.
    """
    urllib.request.urlopen('http://pypi.org/')
