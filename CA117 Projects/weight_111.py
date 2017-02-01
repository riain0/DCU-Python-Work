class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    def to_ounces(self):
        return self.pounds * self.OUNCES_PER_POUND + self.ounces

    def __str__(self):
        return "{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces)

    def __add__(self, other):
        return self.from_ounces(self.to_ounces() + other.to_ounces())

    def __iadd__(self, other):
        c = self + other
        self.pounds = c.pounds
        self.ounces = c.ounces
        return self

    def __mul__(self, other):
        return self.from_ounces(self.to_ounces() * other)
    
    def __imul__(self, other):
        c = self * other
        self.pounds = c.pounds
        self.ounces = c.ounces
        return self
    
    def __rmul__(self, other):
        return self.from_ounces(self.to_ounces() * other)

    def __sub__(self, other):
        return self.from_ounces(self.to_ounces() - other.to_ounces())
    
    def __isub__(self, other):
        c = self - other
        self.pounds = c.pounds
        self.ounces = c.ounces
        return self
    
    def __gt__(self, other):
        return self.to_ounces() > other.to_ounces()
    
    def __ge__(self, other):
        return self.to_ounces() >= other.to_ounces()
    
    def __eq__(self, other):
        return ((self.pounds, self.ounces) == (other.pounds, other.ounces))
    
    @classmethod
    def from_ounces(cls, ounces):
        pounds, ounces = divmod(ounces, cls.OUNCES_PER_POUND)
        return cls(pounds, ounces)