#! /usr/bin/python

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum
For example, given the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous subarray [4,-1,2,1] has the largest sum = 6
'''

class Solution:
    def maxSubArray(self, A):
        size = len(A)
        if size == 0:
            return 0
        sum  = A[0]
        curr_sum = 0
        for index in range(size):
            curr_sum  += A[index]
            sum        = max(curr_sum, sum)
            curr_sum   = max(curr_sum, 0)
        return sum

if __name__ == '__main__':
    solution = Solution()
    print solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print solution.maxSubArray([-1,-2,-3])
