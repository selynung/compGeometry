from point import Point
from convexhull import ConvexHull

def test_convexhull():
    points = []
    points.append(Point(0, 3))
    points.append(Point(2, 2))
    points.append(Point(1, 1))
    points.append(Point(2, 1))
    points.append(Point(3, 0))
    points.append(Point(0, 0))
    points.append(Point(3, 3))

    hull = ConvexHull(points)
    #print(hull.convexHull())
    assert hull.convexHull() == [(0,3),(0,0),(3,0),(3,3)]