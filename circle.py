import math

class circle(object):

    def __init__(self, r):
        self.radius = r

    def area_of_cir(self):
        return math.pi * (self.radius) ** 2

