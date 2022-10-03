class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
       return (self.x, self.y)