"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = list()
        if not matrix:
            return output
        M, N = len(matrix), len(matrix[0])
        m, n = 0, 0
        dirs = ( (-1, 1), (1, -1) )
        index = 0
        while len(output) < M * N:
            output.append( matrix[m][n] )
            m, n = m + dirs[index][0], n + dirs[index][1]
            if (m >= M):
                m, n, index = M - 1, n + 2, 1 - index
            if (n >= N):
                m, n, index = m + 2, N - 1, 1 - index
            if (m < 0):
                m, index = 0, 1 - index
            if (n < 0):
                n, index = 0, 1 - index
        return output

solution = Solution()
print solution.findDiagonalOrder([ [1,2,3], [4,5,6], [7,8,9] ])
