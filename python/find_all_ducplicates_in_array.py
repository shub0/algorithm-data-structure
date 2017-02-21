"""
Given an array of integers, 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = list()
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= (-1)
            else:
                output.append(abs(num))
        return output


nums = [4,3,2,7,8,2,3,1]
solution = Solution()
print solution.findDuplicates(nums)
