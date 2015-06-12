#! /usr/bin/python

'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        size = len(height)
        if size < 2:
            return 0
        max_area = 0
        start = 0
        end   = size - 1
        while start < end:
            curr_area = min(height[start], height[end]) * (end - start)
            max_area = max(max_area, curr_area)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area

if __name__ == '__main__':
    solution = Solution()
    print solution.maxArea([9,6,14,11,2,2,4,9,3,8])
