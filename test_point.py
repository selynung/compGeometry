from point import Point

def test_point():
    x, y = 1, 2
    a = Point(x, y)
    assert a.get_point() == (1, 2)

