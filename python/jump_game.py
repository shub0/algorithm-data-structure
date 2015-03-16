#! /usr/bin/python

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

Problem 2:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
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
            if last_position < index:
                return False
            last_position = max(last_position, A[index] + index)
        return last_position >= size - 1

    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        MAX_INT = 2e9
        size = len(A)
        if size == 0:
            return 0
        dp_array = [MAX_INT] * size
        last_position = 0
        dp_array[0]=0
        for index in range(0, size - 1):
            print dp_array
            if last_position < index:
                return MAX_INT
            if A[index]+index > last_position:
                last_position = A[index]+index
                for cur_index in range(index+1, min(last_position+1, size)):
                    dp_array[cur_index] = min(dp_array[cur_index], dp_array[index]+1)
        return dp_array[-1]

if __name__ == '__main__':
    solution = Solution()
    print solution.jump([2,3,1,1,4])
