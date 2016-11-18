'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        n = len(matrix)
        if k > n * n or n < 1:
            return 0
        heap = list()
        for index in range(n):
            heapq.heappush(heap, (matrix[0][index], 0, index))
        loc = (0, 0, 0)
        while k > 0 and len(heap) > 0:
            k -= 1
            loc = heapq.heappop(heap)
            if loc[1] < n-1:
                row = loc[1] + 1
                col = loc[2]
                element = matrix[row][col]
                heapq.heappush(heap, (element, row, col))
        return loc[0]


solution = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
print solution.kthSmallest(matrix, 8)
