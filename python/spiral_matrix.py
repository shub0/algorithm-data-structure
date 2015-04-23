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

Follow up:
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
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

    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        output = list()
        if not matrix:
            return output
        ROW = len(matrix)
        COL = len(matrix[0])
        SIZE = ROW * COL
        direct_index = 0
        direction = [ (0,1), (1,0), (0,-1), (-1,0) ]
        curr_row = 0
        curr_col = -1
        index = 0
        VISITED = -1e10
        while index < SIZE:
            next_row = curr_row + direction[direct_index][0]
            next_col = curr_col + direction[direct_index][1]
            if next_row < ROW and next_col < COL and matrix[next_row][next_col] != VISITED:
                curr_row = next_row
                curr_col = next_col
                output.append(matrix[curr_row][curr_col])
                matrix[curr_row][curr_col] = VISITED
                index += 1
            else:
                direct_index += 1
                direct_index %= 4
        return output
if __name__ == '__main__':
    solution = Solution()
    matrix = solution.generateMatrix(5)
    print solution.spiralOrder(matrix)
