'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
Given m satisfies the following constraint: 1 <= m <= len(nums) <= 14,000.

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''

class Solution(object):
    def valid(self, nums, m, val):
        cnt = 1
        curr = 0
        for num in nums:
            curr += num
            if curr > val:
                cnt += 1
                curr = num
                # val is too small
                if cnt > m:
                    return False
        return True

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (right - left) / 2 + left
            if self.valid(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return left


solution = Solution()
print solution.splitArray([7,2,5,10,8], 2)
print solution.splitArray([7,2,5,10,8], 3)
print solution.splitArray([7,2,10,5,8], 2)
print solution.splitArray([1,4,4], 3)
