#! /usr/bin/python

'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

from Interval import Interval
class Solution:
    def insert(self, intervals, new):
        """
        :type intervals: List[Interval]
        :type new: Interval
        :rtype: List[Interval]
        """
        size = len(intervals)
        output = list()
        inserted = False
        index = 0
        while index < size:
            curr = intervals[index]
            # no overlapping
            if not inserted and curr.end < new.start:
                output.append(curr)
                index += 1
                continue
            if inserted:
                new = curr
                index += 1
            inserted = True
            # overlapping
            while len(output) > 0 and output[-1].end >= new.start:
                last = output.pop()
                new.start = min(new.start, last.start)
                new.end = max(new.end, last.end)
            output.append(new)

        if not inserted:
            output.append(new)
        return output

if __name__ == '__main__':
    solution = Solution()
    a_list = [Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10),Interval(12,16)]
    b_list = solution.insert1(a_list, Interval(4,9))
    print "Expected [[1, 2], [3, 10], [12, 16]], got "
    print b_list
