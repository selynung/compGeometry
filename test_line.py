from point import Point
from line import Line

def test_point():
    x1, y1, x2, y2 = 0, 0, 3, 4
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    l = Line(p1, p2)
    assert l.length() == 5


