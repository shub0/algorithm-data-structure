#! /usr/bin/python

'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

from Interval import Interval
class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        import operator
        output = list()
        size = len(intervals)
        if size == 0:
            return output
        intervals.sort(key=operator.attrgetter('end'))
        start = intervals[0].start
        end   = intervals[0].end
        output.append(intervals[0])
        for index in range(1,size):
            current_interval = intervals[index]
            # No overlapping
            if end < current_interval.start:
                output.append(current_interval)
                end = current_interval.end
                continue
            # overlapping
            while len(output) > 0 and output[-1].end >= current_interval.start:
                last_interval = output.pop()
                start = min(current_interval.start, last_interval.start)
                end = max(current_interval.end, current_interval.end)
            output.append(Interval(start, end))
        return output

if __name__ == '__main__':
    solution = Solution()
    a_list = [Interval(1,3), Interval(2,6), Interval(3,5), Interval(8,10), Interval(15,18), Interval(5,9)]
    b_list = [Interval(1,4),  Interval(0,4)]
    print solution.merge(a_list)
    print solution.merge(b_list)
