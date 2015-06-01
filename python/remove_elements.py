#! /usr/bin/python

'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        end = len(nums) - 1
        start = 0
        while start < end:
            while nums[start] != val and start < end:
                start += 1
            while nums[end] == val and start < end:
                end -= 1
            nums[start], nums[end] = nums[end], nums[start]
        if len(nums) == 0:
            return 0
        if nums[-1] == val:
            return start
        return start + 1


if __name__ == '__main__':
    solution = Solution()
    nums = []
    new_len = solution.removeElement(nums,3)
    print 'len = %d' % new_len
    print nums[:new_len]
