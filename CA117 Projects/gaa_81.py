class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return("{} goal(s) and {} point(s)".format(self.goals, self.points))

    def total(self):
        return (self.goals * 3) + self.points

    def __eq__(self, other):
        return self.total() == other.total()

    def __gt__(self, other):
        return self.total() > other.total()

    def __ge__(self, other):
        return self.total() >= other.total()

    def __add__(self, other):
        return self.total() + other.total()

    def __sub__(self, other):
        return self.total() - other.total()

    def __iadd__(self, other):
        return self.total() += other.total()

    def __isub__(self, other):
        return self.total() -= other.total()
