class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def distance(self, p2):
        return ((p2.x - self.x)**2 + (p2.y - self.y)**2)*0.5


    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def midpoint(self):
        return ((self.p1.x + self.p2.x)/2, (self.p1.y + self.p2.y)/2)


    def length(self):
        return p1.distance(p2)


class Circle(object):

    def __init__(self, centre, radius):
        self.radius = radius
        self.centre = centre


    def overlaps(self, other):
        return self.centre.distance(other.centre) < (self.radius + other.radius)
