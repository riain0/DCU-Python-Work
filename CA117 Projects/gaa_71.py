class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points


    def greater_than(self, score2):
        p1 = (self.goals * 3) + self.points
        p2 = (score2.goals * 3) + score2.points
        if p1 > p2:
            return True
        return False


    def less_than(self, score2):
        p1 = (self.goals * 3) + self.points
        p2 = (score2.goals * 3) + score2.points
        if p1 < p2:
            return True
        return False


    def equal_to(self, score2):
        p1 = (self.goals * 3) + self.points
        p2 = (score2.goals * 3) + score2.points
        if p1 == p2:
            return True
        return False
