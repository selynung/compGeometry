from circle import Circle
from point import Point
from line import Line

def test_circle():
    x1, y1, x2, y2 = 0, 0, 3, 4
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    r = Line(p1, p2)
    c = Circle(r)
    assert "{:.2f}".format(c.area_of_cir()) == 78.53