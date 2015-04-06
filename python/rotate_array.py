#! /usr/bin/python

'''
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Could you do it in-place with O(1) extra space?
'''

class Solution:
    def rotateInPlace(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        size = len(nums)
        if size < 2:
            return
        k   %= size
        self.rotateInPlace(nums, 0, size - 1)
        self.rotateInPlace(nums, 0, k-1)
        self.rotateInPlace(nums, k, size-1)
        print nums


if __name__ == '__main__':
    solution = Solution()
    print solution.rotate(range(1,8), 3)
