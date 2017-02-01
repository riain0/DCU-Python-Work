class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def reflect(self):
        self.x = -(self.x)
        self.y = -(self.y)


    def distance(self, p2):
        dist = (((p2.x - self.x) ** 2) + ((p2.y + self.y) ** 2)) ** 0.5
        return dist
