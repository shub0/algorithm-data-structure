#! /usr/bin/python

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        row    = len(grid)
        column = len(grid[0])
        dp_array = [ [0] * column for index in range(row) ]
        for index_row in range(row):
            for index_column in range(column):
                if index_row == 0 and index_column == 0:
                    dp_array[index_row][index_column] = grid[index_row][index_column]
                elif index_row == 0:
                    dp_array[0][index_column] = dp_array[0][index_column-1] + grid[0][index_column]
                elif index_column == 0:
                    dp_array[index_row][0] = grid[index_row][0] + dp_array[index_row-1][0]
                else:
                    dp_array[index_row][index_column] = min(dp_array[index_row-1][index_column], dp_array[index_row][index_column-1]) + grid[index_row][index_column]
        return dp_array[-1][-1]

if __name__ == '__main__':
    grid = [[1,2,3,4],[4,5,6,7], [8,9,10,11]]
    solution = Solution()
    print solution.minPathSum(grid)
