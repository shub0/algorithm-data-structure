'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_array = list()
        indices = list()
        size = len(nums)
        if size == 0 or k > size:
            return []
        for index in range(k):
            while (len(indices) > 0) and (nums[index] >= nums[indices[-1]]):
                indices.pop()
            indices.append(index)
        for index in range(k, size):
            max_array.append(nums[indices[0]])
            while (len(indices) > 0) and (nums[index] >= nums[indices[-1]]):
                indices.pop()
            indices.append(index)
            while (len(indices) > 0) and (indices[0] <= index - k):
                del indices[0]
        max_array.append(nums[indices[0]])
        return max_array
