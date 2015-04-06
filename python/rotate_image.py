#! /usr/bin/python

'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        N = len(matrix)
        if N < 2:
            return
        matrix[:] = zip(*matrix[::-1])
        matrix[:] = [ list(array) for array in matrix ]
        print matrix

    def rotateInPlace(self, matrix):
        return

if __name__ == '__main__':
    solution = Solution()
    solution.rotate([[1]])
    solution.rotate([[1,2,3],[4,5,6],[7,8,9]])

