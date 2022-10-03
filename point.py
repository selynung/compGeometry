class Point(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
       return (self.x, self.y)

    def __str__(self):
        return (self.x, self.y)

    __repr__ = __str__