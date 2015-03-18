#! /usr/bin/python

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

'''

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        dp_array = [ [0] * n for index in range(m) ]
        for index in range(n):
            dp_array[0][index] = 1
        for index in range(m):
            dp_array[index][0] = 1
        for index_n in range(1, n):
            for index_m in range(1, m):
                dp_array[index_m][index_n] = dp_array[index_m-1][index_n] + dp_array[index_m][index_n-1]
        return dp_array[-1][-1]

    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        dp_array = [ [0] * num_cols for index in range(num_rows) ] 
        if obstacleGrid[0][0] == 1:
            return 0
        for index in range(0,num_cols):
            if obstacleGrid[0][index] == 1:
                break
            dp_array[0][index] = 1
        for index in range(0, num_rows):
            if obstacleGrid[index][0] == 1:
                break
            dp_array[index][0] = 1
        for index_col in range(1, num_cols):
            for index_row in range(1, num_rows):
                if obstacleGrid[index_row][index_col] == 1:
                    dp_array[index_row][index_col] = 0
                else:
                    dp_array[index_row][index_col] = dp_array[index_row-1][index_col] + dp_array[index_row][index_col-1]
        return dp_array[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    print solution.uniquePaths(3,7)
