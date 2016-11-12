'''
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[%d, %d]" % (self.start, self.end)

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.data = collections.OrderedDict()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        self.data[val] = val

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        values = sorted(self.data.keys())
        print values
        output = list()
        size = len(values)
        if size < 1:
            return output
        start = values[0]
        for index in range(1, size):
            if values[index] != values[index-1] + 1:
                output.append(Interval(start, values[index-1]))
                start = values[index]
        output.append(Interval(start, values[-1]))
        return output


# Your SummaryRanges object will be instantiated and called as such:
values = [1,3,7,2,6, 9, 3]
obj = SummaryRanges()
[obj.addNum(val) for val in values]
print obj.getIntervals()
