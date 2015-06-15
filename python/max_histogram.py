#! /usr/bin/python

'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        size = len(height)
        if size == 0:
            return 0
        min_stack = list()
        max_area = height[0]
        for index in range(size):
            if len(min_stack) == 0 or min_stack[-1][0] <= height[index]:
                min_stack.append((height[index], index))
            else:
                while len(min_stack) > 0 and min_stack[-1][0] > height[index]:
                    pair = min_stack.pop()
                    temp_area = pair[0] * (index - pair[1])
                    max_area = max(max_area, temp_area)
                min_stack.append((height[index], pair[1]))

        while len(min_stack) > 0:
            pair = min_stack.pop()
            temp_area = pair[0] * (size - pair[1])
            max_area = max(temp_area, max_area)
        return max_area

if __name__ == '__main__':
    solution = Solution()
    print solution.largestRectangleArea([2,1,5,6,2,3])
