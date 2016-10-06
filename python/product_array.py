'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        left = [1] * size
        right = [1] * size
        start = 1
        for index in range(1, size):
            start *= nums[index-1]
            left[index] = start
        start = 1
        for index in range(size-2, -1, -1):
            start *= nums[index+1]
            right[index] = start
        output = [0] * size
        for index in range(size):
            output[index] = left[index] * right[index]
        return output

solution = Solution()
print solution.productExceptSelf([0,2,3])
