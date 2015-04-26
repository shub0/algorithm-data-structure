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
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, new_interval):
        size = len(intervals)
        new_intervals = list()
        if size == 0:
            return [new_interval]
        start = new_interval.start
        end   = new_interval.end
        index = 0
        insert_flag = False
        while index < size:
            current_interval = intervals[index]
            # no overlapping
            if insert_flag or start > current_interval.end:
                new_intervals.append(current_interval)
                index += 1
                continue
            while index < size:
                current_interval = intervals[index]
                if start > current_interval.end or end < current_interval.start:
                    break
                start = min(start, current_interval.start)
                end   = max(end, current_interval.end)
                index += 1
            new_intervals.append(Interval(start, end))
            insert_flag = True

        if not insert_flag:
            new_intervals.append(Interval(start, end))
        return new_intervals

if __name__ == '__main__':
    solution = Solution()
    a_list = [Interval(1,3), Interval(8,10), Interval(15,18)]
    b_list = solution.insert(a_list, Interval(4,9))
    print b_list
