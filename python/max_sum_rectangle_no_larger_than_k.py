'''
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
'''

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import sys
        import bisect
        row = len(matrix)
        col = len(matrix[0]) if row > 0 else 0
        M = max(row, col)
        N = min(row, col)
        res = None
        for start in range(N):
            sums = [0] * M
            for end in range(start, N):
                slist, curr = [], 0
                for m in range(M):
                    sums[m] += matrix[m][end] if row > col else matrix[end][m]
                    curr += sums[m]
                    if curr <= k:
                        res = max(res, curr)
                    index = bisect.bisect_left(slist, curr - k)
                    if index < len(slist):
                        res = max(res, curr - slist[index])
                    bisect.insort(slist, curr)
        return res or 0

solution = Solution()
matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
print solution.maxSumSubmatrix(matrix, 10)
