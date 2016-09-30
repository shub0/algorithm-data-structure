#! /usr/bin/python

'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
from node_struct import PointNode
class Solution:
    def findLine(self, a, b):
        if a.x == b.x:
            slope = float('inf')
            intersection = a.x
        else:
            slope = 1.0 * (a.y - b.y) / (b.x - a.x)
            intersection = 1.0 * (a.y*b.x - a.x*b.y) / (b.x-a.x)
        return (slope, intersection)

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import collections
        size = len(points)
        lines = collections.defaultdict(set)
        for index_start in range(1, size):
            for index_end in range(index_start):
                line = self.findLine(points[index_start], points[index_end])
                lines[line].add(points[index_start])
                lines[line].add(points[index_end])
        if len(lines) < 1:
            return size
        return max([ len(s) for s in lines.values() ])

if __name__=='__main__':
    solution = Solution()
    p1 = PointNode(1,1)
    p2 = PointNode(2,2)
    p3 = PointNode(3,3)
    p4 = PointNode(4,2)
    p5 = PointNode(3,5)
    print len(solution.maxPoints([p1, p2, p3, p4, p5]))
    #print (PointNode(1,1) == PointNode(1,1))
