#! /usr/bin/python

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        size = len(height)
        left = [0] * size
        right = [0] * size
        max_height = 0
        for index in range(size):
            left[index] = max_height
            max_height = max(height[index], max_height)
        max_height = 0
        for index in range(size-1, -1, -1):
            right[index] = max_height
            max_height = max(height[index], max_height)
        sum = 0
        for index in range(size):
            temp = min(left[index], right[index]) - height[index]
            if temp > 0:
                sum += temp
        return sum

if __name__ == '__main__':
    solution = Solution()
    print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
