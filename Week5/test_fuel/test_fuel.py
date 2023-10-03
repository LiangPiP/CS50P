from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0

    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(100)=="F"
    assert gauge(99)=="F"
    assert gauge(1)=="E"
    assert gauge(0)=="E"
    assert gauge(25)=="25%"