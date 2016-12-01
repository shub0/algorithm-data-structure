'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import collections
        nums = 0
        for x1, y1 in points:
            distance = collections.defaultdict(int)
            for x2, y2 in points:
                dx = x2 - x1
                dy = y2 - y1
                d = dx * dx + dy * dy
                distance[d] += 1

            nums += sum(n * (n-1) for n in distance.values())
        return nums

solution = Solution()
print solution.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
