#! /usr/bin/python

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) < 2:
            return True
        elif len(A) == 2:
            return A[0] > 0
        size = len(A)
        last_position = 0
        for index in range(0, size - 1):
            print last_position
            if last_position < index:
                return False
            last_position = max(last_position, A[index] + index)
        return last_position >= size - 1

if __name__ == '__main__':
    solution = Solution()
    print solution.canJump([2,3,1,1,4])
    print solution.canJump([3,2,1,0,4])
    print solution.canJump([0,2,3])
