'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        nums.sort()
        target = total / 2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            index = target
            while index >= num:
                dp[index] = (dp[index] or dp[index - num])
                index -= 1
        return dp[target]

solution = Solution()
print solution.canPartition([1,5,11,5])
print solution.canPartition([1,2,3,5])
print solution.canPartition([1,2,5])
