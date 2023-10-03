from um import count

def test_count():
    assert count("um")==1
    assert count("um?")==1
    assert count("yummy")==0
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2
    assert count(" Um um um")==3
    assert count(" umum")==0
    assert count("You ar um good")==1
    assert count("hello world")==0
