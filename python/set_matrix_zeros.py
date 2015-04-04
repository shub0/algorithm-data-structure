#! /usr/bin/python

'''
 Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        row_flag = False
        col_flag = False
        # TODO Iterate 2D array columnize
        for index in range(col):
            if matrix[0][index] == 0:
                row_flag = True
        for index in range(row):
            if matrix[index][0] == 0:
                col_flag = True

        for index_row in range(1, row):
            for index_col in range(1, col):
                if matrix[index_row][index_col] == 0:
                    matrix[index_row][0] = 0
                    matrix[0][index_col] = 0

        for index_col in range(1,col):
            if matrix[0][index_col] == 0:
                for index_row in range(row):
                    matrix[index_row][index_col] = 0

        for index_row in range(1, row):
            if matrix[index_row][0] == 0:
                for index_col in range(col):
                    matrix[index_row][index_col] = 0

        if row_flag:
            for index_col in range(col):
                matrix[0][index_col] = 0

        if col_flag:
            for index_row in range(row):
                matrix[index_row][0] = 0

if __name__ == '__main__':
   # matrix = [[2,3,0,6,7], [5,8,1,9,8],[6,0,3,2,3],[1,3,4,1,1]]
    matrix = [[1,2,0,4]]
    solution = Solution()
    solution.setZeroes(matrix)
    print matrix
