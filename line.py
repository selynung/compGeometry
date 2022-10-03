from point import Point
import math

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        line = "((%f,%f),(%f,%f))" % (x1, y1, x2, y2)
        return line

    __repr__ = __str__

    def length(self):
        dist_x = abs(self.p2.x - self.p1.x)
        dist_y = abs(self.p2.y - self.p1.y)
        dist_x_squared = dist_x ** 2
        dist_y_squared = dist_y ** 2
        line_length = math.sqrt(dist_x_squared + dist_y_squared)
        return line_length

    def slope(self):
        dist_y = self.p2.y - self.p1.y
        dist_x = self.p2.x - self.p1.x
        line_slope = dist_y / dist_x
        return line_slope