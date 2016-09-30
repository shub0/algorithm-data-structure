#! /usr/bin/python

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if (size == 0):
            return 0
        max_product = nums[0]
        min_product = nums[0]
        curr_max_product = nums[0]
        for num in nums[1:]:
            if num >= 0:
                max_product, min_product = max(num, num * max_product), min(num, num * min_product)
            else:
                max_product, min_product = max(num, num * min_product), min(num, num * max_product)
            curr_max_product = max(curr_max_product, max_product)
        return curr_max_product
if __name__ == '__main__':
    solution = Solution()
    print solution.maxProduct([2,3,-2,4])
