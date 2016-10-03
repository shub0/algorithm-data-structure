'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''

class Solution(object):
    # O(n) solution
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        size = len(nums)
        curr_sum = 0
        min_size = size + 1
        while right < size:
            curr_sum += nums[right]
            right += 1
            while (curr_sum >= s):
                min_size = min(right - left, min_size)
                curr_sum -= nums[left]
                left += 1
        return 0 if min_size > size else min_size

    def search(self, nums, target):
        # search the last index of element < target
        left = 0
        right = len(nums) - 1
        pos = right
        while left < right:
            mid = (right - left) / 2 + left
            if nums[mid] < target:
                left = mid + 1
                pos = mid
            else:
                right = mid
        return pos if nums[pos] < target else -1

    # O(NlogN) soltuion
    def minSubArrayLen2(self, s, nums):
        size = len(nums)
        min_len = size + 1
        sum_array = [sum(nums[:index+1]) for index in range(size)]
        print sum_array
        for index in range(size):
            if sum_array[index] < s:
                continue
            target = sum_array[index] - s + 1
            start = self.search(sum_array, target)
            min_len = min(min_len, index-start)
        return 0 if min_len > size else min_len

solution = Solution()
min_len = solution.minSubArrayLen2(13, [1,2,3,4,5])
print min_len
#solution.search([1, 3, 6, 10, 15], 1)
