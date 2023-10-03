from seasons import convert
from datetime import date

def test_convert():
    assert convert(date(2001,7,2))=="Eleven million, seven hundred two thousand, eight hundred eighty minutes"
    assert convert(date(2022,10,2))=="Five hundred twenty-five thousand, six hundred minutes"