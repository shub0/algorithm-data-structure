# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        size = len(intervals)
        output = list()
        if size == 0:
            return output
        intervals.sort(key=lambda x: x.end)
        for index in range(size):
            curr = intervals[index]
            while len(output) > 0 and curr.start <= output[-1].end:
                last = output.pop()
                curr.start = min(last.start, curr.start)
                curr.end = max(last.end, curr.end)
            output.append(curr)
        return output

if __name__ == '__main__':
    solution = Solution()
    a_list = [Interval(1,3), Interval(2,6), Interval(3,5), Interval(8,10), Interval(15,18), Interval(5,9)]
    b_list = [Interval(1,4),  Interval(0,4)]
    print solution.merge(a_list)
    print solution.merge(b_list)
