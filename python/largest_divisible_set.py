'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
'''

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        if size < 2:
            return nums
        nums.sort()
        dp_size = [0] * size
        dp_anc = [-1] * size
        for index in range(size):
            max_size = 0
            max_anc = -1
            for idx in range(index):
                if nums[idx] > 0 and nums[index] % nums[idx] == 0 and dp_size[idx] > max_size:
                    max_anc = idx
                    max_size = dp_size[idx]
            dp_size[index] = max_size + 1
            dp_anc[index] = max_anc
        max_size =  max(dp_size)
        idx = dp_size.index(max_size)
        output = list()
        while (dp_anc[idx] >= 0):
            output.append(nums[idx])
            idx = dp_anc[idx]
        if (not output or output[-1] % nums[idx] == 0):
            output.append(nums[idx])
        return output[::-1]

solution = Solution()
print solution.largestDivisibleSubset([1,2,3,4,8,9,27,81])
print solution.largestDivisibleSubset([])
print solution.largestDivisibleSubset([1])
