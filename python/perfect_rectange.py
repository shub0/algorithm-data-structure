'''
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
'''


class Solution(object):
    # Inner points must present even times
    # Corner points must present only once
    # Total area must be the sum of each rectangle
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        import collections
        def getSize(rectangle):
            return abs(rectangle[0] - rectangle[2]) * abs(rectangle[1] - rectangle[3])
        def recordPoint(rectangle):
            points[ (rectangle[0], rectangle[1]) ] += 1
            points[ (rectangle[2], rectangle[3]) ] += 1
            points[ (rectangle[0], rectangle[3]) ] += 1
            points[ (rectangle[2], rectangle[1]) ] += 1

        points = collections.defaultdict(int)
        area = 0
        L, B, R, T = float("inf"), float("inf"), float("-inf"), float("-inf")
        for rectangle in rectangles:
            L, B, R, T = min(rectangle[0], L), min(rectangle[1], B), max(rectangle[2], R), max(rectangle[3], T)
            area += getSize(rectangle)
            recordPoint(rectangle)
        if area != getSize( (L, B, R, T) ):
            return False
        corners = { (L, B), (L, T), (R, B), (R, T) }
        if any(points[corner] != 1 for corner in corners):
            return False
        if any(points[point] %2 != 0 for point in points if point not in corners):
            return False
        return True
