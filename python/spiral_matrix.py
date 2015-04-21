#! /usr/bin/python

'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        num = 1
        matrix = [ [0] * n for index in range(n) ]
        direction = [ (0,1), (1,0), (0,-1), (-1,0) ]
        size = n * n
        row = 0
        col = -1
        direct_index = 0
        while num <= size:
            next_row = row + direction[direct_index][0]
            next_col = col + direction[direct_index][1]
            if next_row < n and next_col < n and matrix[next_row][next_col] == 0:
                row = next_row
                col = next_col
                matrix[row][col] = num
                num += 1
            else:
                direct_index += 1
                direct_index %= 4
        return matrix

if __name__ == '__main__':
    solution = Solution()
    print '\n'.join([ str(line) for line in solution.generateMatrix(5)])
