'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        LIS = [1] * size
        if size < 2:
            return size
        for (index, num) in enumerate(nums):
            prev = [ LIS[i] for i in range(index) if nums[i] < num ]
            LIS[index] = 1 + max(prev) if prev else 1
        return max(LIS)

    def binarySearch(self, array, num):
        left = 0
        right = len(array)-1
        while left < right:
            mid = (left + right) / 2
            if array[mid] >= num:
                right = mid
            else:
                left = mid+1
        return right

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2:
            return size
        stack = [nums[0]]
        for index in range(1, size):
            if nums[index] > stack[-1]:
                stack.append(nums[index])
            else:
                last_index = self.binarySearch(stack, nums[index])
                stack[last_index] = nums[index]
        return len(stack)

solution = Solution()
print solution.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18])
