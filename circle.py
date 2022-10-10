import math

class Circle(object):

    def __init__(self, center,  r):
        self.center = center
        self.radius = r

    def area_of_cir(self):
        return math.pi * (self.radius) ** 2

