#! /usr/bin/python

'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
import math
class Solution:
    # @param numRows, an integer
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        pascal_triangle = list()
        curr_row = [1]
        pascal_triangle.append(curr_row)
        for row_index in range(1, numRows):
            curr_row = [0] * (row_index + 1)
            curr_row[0] = 1
            curr_row[-1] = 1
            for column_index in range(1, row_index):
                curr_row[column_index] = pascal_triangle[row_index - 1][column_index - 1] + pascal_triangle[row_index - 1][column_index]
            pascal_triangle.append(curr_row)
        return pascal_triangle

    # @param n, an integer
    # @param k, an integer
    # @return an integer
    def getCombinational(self, n, k):
        return math.factorial(n) / math.factorial(n - k) / math.factorial(k)
    
    # @param rowIndex, an integer
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
             return [1]
        prev_row = [1]
        for curr_row_index in range(1, rowIndex + 1):
            curr_row = [0] * (curr_row_index + 1)
            curr_row[0] = 1
            curr_row[-1] = 1
            for column_index in range(1, curr_row_index):
                curr_row[column_index] = prev_row[column_index - 1] + prev_row[column_index]
            prev_row = curr_row
        return prev_row

if __name__ == '__main__':
    solution = Solution()
    print solution.generate(7)
    print solution.getRow(3)
