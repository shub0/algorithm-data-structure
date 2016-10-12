'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
[3,0,1,4,2],
[5,6,3,2,1],
[1,2,0,1,5],
[4,1,0,1,7],
[1,0,3,0,5]

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8
'''

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        self.empty = False
        if row < 0:
            self.empty = True
        col = len(matrix[0])
        self.dp = [ [0] * col for _ in range(row) ]
        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0:
                    self.dp[r][c] = matrix[r][c]
                elif r == 0:
                    self.dp[r][c] = matrix[r][c] + self.dp[r][c-1]
                elif c == 0:
                    self.dp[r][c] = matrix[r][c] + self.dp[r-1][c]
                else:
                    self.dp[r][c] = self.dp[r-1][c] + self.dp[r][c-1] + matrix[r][c] - self.dp[r-1][c-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        elif row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        elif col1 == 0:
            return self.dp[row2][col2] - self.dp[row1-1][col2]
        else:
            return self.dp[row2][col2] + self.dp[row1-1][col1-1] - self.dp[row2][col1-1] - self.dp[row1-1][col2]


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3,0,1,4,2],
          [5,6,3,2,1],
          [1,2,0,1,5],
          [4,1,0,1,7],
          [1,0,3,0,5]
]

numMatrix = NumMatrix(matrix)
print numMatrix.dp
print numMatrix.sumRegion(1, 0, 2, 3)
print numMatrix.sumRegion(1, 2, 3, 4)
