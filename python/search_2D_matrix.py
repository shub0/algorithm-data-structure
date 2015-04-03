#! /usr/bin/python

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true.
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end   = m * n - 1
        while start <= end:
            mid     = start + (end - start) / 2
            mid_row = mid / n
            mid_col = mid % n
            if matrix[mid_row][mid_col] < target:
                start = mid + 1
            elif matrix[mid_row][mid_col] > target:
                end = mid - 1
            else:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
