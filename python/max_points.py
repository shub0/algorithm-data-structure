#! /usr/bin/python

'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
from node_struct import PointNode
class Solution:
    # @param a, a point location on 2D plane
    # @param b, a point location on 2D plane
    # @retrun a float pair describe a line on 2D plane
    @classmethod
    def findLine(cls, a, b):
        if (a.x == b.x and a.y == b.y) or (a.x == b.x and a.x == 0):
            return (0.0, 0.0)
        elif a.x == b.x:
            slope = 0
            intersection = -1.0 / a.x
        else:
            slope = 1.0 * (a.y - b.y) / (b.x - a.x)
            intersection = 1.0 * (a.y*b.x - a.x*b.y) / (b.x-a.x)
        return (slope, intersection)

    # @param line, a line(a,b) as ax+y+b = 0
    # @param point, a point location on 2D plane
    # @retrun, if point is on the line
    @classmethod
    def fitLine(cls, line, point):
        return (line[0] * point.x + point.y + line[1] == 0)

    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        size = len(points)
        line_dict = {}
        if (size == 0):
            return None
        if (size == 1):
            return points[0]
        for index_start in range(size-1):
            for index_end in range(index_start, size):
                if points[index_start].x == points[index_end].x and points[index_start].y == points[index_end].y:
                    continue
                line = Solution.findLine(points[index_start], points[index_end])
                if line not in line_dict.keys():
                    line_dict[line] = 1
                else:
                    line_dict[line] += 1
        max_points_count = 0
        max_line = (0,0)
        point_on_line = list()
        for line in line_dict.keys():
            count = line_dict[line]
            if count > max_points_count:
                max_points_count = count
                max_line = line
        for point in points:
            if (Solution.fitLine(max_line, point)):
                point_on_line.append(point)
        return point_on_line
        
if __name__=='__main__':
    solution = Solution()
    p1 = PointNode(1,1)
    p2 = PointNode(2,2)
    p3 = PointNode(3,3)
    p4 = PointNode(4,2)
    p5 = PointNode(3,5)
    print len(solution.maxPoints([p1, p2, p3, p4, p5]))
    #print (PointNode(1,1) == PointNode(1,1))
