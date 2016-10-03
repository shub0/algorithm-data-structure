'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Follow up quetions:
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        if size <= 2:
            return max(nums)
        # Dynamic programming
        rob = [0] * size
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])
        for index in range(2,size):
            rob[index] = max(nums[index] + rob[index-2], rob[index-1])

        return rob[-1]

    def rob2(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        if size <= 2:
            return max(nums)
        #Dynamic programming
        rob = [0] * size
        rob[0] = nums[0]
        rob[1] = nums[0]
        for index in range(2, size):
            rob[index] = max(nums[index] + rob[index-2], rob[index-1])
        money = rob[-2]
        rob[0] = 0
        rob[1] = nums[1]
        for index in range(2, size):
            rob[index] = max(nums[index] + rob[index-2], rob[index-1])
        return max(money, rob[-1])
