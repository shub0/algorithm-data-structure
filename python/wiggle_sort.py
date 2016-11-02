'''
Given an unsorted array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
(1) Can you do it in O(n) time and/or in-place with O(1) extra space?
(2) Can you do it strict wiggle sort such that nums[0] < nums[1] > nums[2] < nums[3]
'''

class Solution(object):
    def findKthElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        if size < k:
            raise ValueError("size of list(%d) is smaller than k(%d)" % (size, k))
        start = 0
        end = size - 1
        while True:
            pivot = nums[start]
            pivot_index = start
            for index in range(start, end+1):
                if nums[index] < pivot:
                    pivot_index += 1
                    nums[index], nums[pivot_index] = nums[pivot_index], nums[index]
            nums[start], nums[pivot_index] = nums[pivot_index], nums[start]

            left_size = pivot_index - start + 1
            # search first half
            if left_size > k:
                end = pivot_index
            # search second half
            elif left_size < k:
                start = pivot_index + 1
                k -= left_size
            else:
                return nums[pivot_index]

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size < 2:
            return nums
        median = self.findKthElement(nums, (size+1) / 2)
        left = 1
        right = size - 1
        while (left < right):
            if nums[left] != nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
            left += 2
            right -= 2

    def wiggleSort2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size < 2:
            return nums
        median = self.findKthElement(nums, (size+1) / 2)
        def indexMap(index):
            return (2*index+1) % (size | 1)
        left, index, right = 0, 0, size-1
        while index <= right:
            if nums[indexMap(index)] > median:
                nums[indexMap(left)], nums[indexMap(index)] = nums[indexMap(index)], nums[indexMap(left)]
                index += 1
                left += 1
            elif nums[indexMap(index)] < median:
                nums[indexMap(right)], nums[indexMap(index)] = nums[indexMap(index)], nums[indexMap(right)]
                right -= 1
            else:
                index += 1

import random
solution = Solution()
nums = [1,1,2,2,3,4]
random.shuffle(nums)
solution.wiggleSort2(nums)
print nums
