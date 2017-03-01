"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.dp = collections.defaultdict(int)
        self.dp["[]->0"] = 1
        return self.helper(nums, S)

    def helper(self, nums, target):
        sig = ("%s->%d" % (str(nums), target))
        if sig in self.dp:
            return self.dp[sig]
        elif not nums:
            return 0
        else:
            res = self.helper(nums[:-1], target - nums[-1])
            res += self.helper(nums[:-1], target + nums[-1])
            self.dp[sig] = res
            return res

    def findTargetSumWays2(self, nums, S):
        total = sum(nums)
        target = S + total
        if target % 2 == 1 or total < S:
            return 0
        target = (target >> 1)
        nums.sort()
        dp = [0] * (target+1)
        dp[0] = 1
        for num in nums:
            for idx in range(target, num-1, -1):
                dp[idx] += dp[idx-num]
        return dp[target]

solution = Solution()
print solution.findTargetSumWays2([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47],38)
#print solution.findTargetSumWays2([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 6)
