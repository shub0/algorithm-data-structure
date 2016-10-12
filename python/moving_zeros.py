'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zeros = 0
        size = len(nums)
        for index in range(size):
            if nums[index] != 0:
                nums[non_zeros] = nums[index]
                non_zeros += 1
        while non_zeros < size:
            nums[non_zeros] = 0
            non_zeros += 1


solution = Solution()
num = [1,1,3,3,12]
solution.moveZeroes(num)
print num
