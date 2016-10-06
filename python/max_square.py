'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ROW = len(matrix)
        if ROW < 1:
            return 0
        COL = len(matrix[0])
        dp_array = [ [0] * COL for _ in range(ROW) ]
        max_size = 0
        for row in range(ROW):
            for col in range(COL):
                if row == 0 or col == 0:
                    dp_array[row][col] = int(matrix[row][col])
                elif matrix[row][col] == '1':
                    dp_array[row][col] = min([dp_array[row-1][col], dp_array[row][col-1], dp_array[row-1][col-1]]) + 1
                max_size = max(max_size, dp_array[row][col] * dp_array[row][col])
        return max_size
