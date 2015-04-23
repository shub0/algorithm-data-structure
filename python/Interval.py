# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return '[%d, %d]' % (self.start, self.end)
