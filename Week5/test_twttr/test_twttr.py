from twttr import shorten

def test_shorten():
    assert shorten("David")=="Dvd"
    assert shorten("1111")=='1111'
    assert shorten("aOENc")=='Nc'
    assert shorten(",")==","