#! /usr/bin/python
'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        size = len(triangle)
        if size == 0:
            return 0
        if size == 1:
            return triangle[0][0]
        prev_minimum_total = triangle[0]
        for row_index in range(1, size):
            curr_row_size = len(triangle[row_index])
            curr_minimum_total = [0] * curr_row_size
            curr_minimum_total[0] = prev_minimum_total[0] + triangle[row_index][0]
            curr_minimum_total[-1]= prev_minimum_total[-1]+ triangle[row_index][-1]
            for column_index in range(1, curr_row_size - 1):
                curr_minimum_total[column_index] = triangle[row_index][column_index] + min(prev_minimum_total[column_index - 1], prev_minimum_total[column_index])
            prev_minimum_total = curr_minimum_total
        return min(prev_minimum_total)

if __name__ == '__main__':
    solution = Solution()
    print solution.minimumTotal([[2], [3,4], [6, 5, 7], [4, 1, 8, 3]])
