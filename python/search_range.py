#! /usr/bin/python

'''
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    def searchPosition(self, num, target):
        start = 0
        end   = len(num) - 1
        pos   = len(num)
        while start <= end:
            middle = (end - start) / 2 + start
            if num[middle] < target:
                start = middle + 1
            else:
                pos = middle
                end = middle - 1
        return pos

    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, num, target):
        index1 = self.searchPosition(num, target)
        index2 = self.searchPosition(num, target+1)-1
        if index1 >= len(num) or num[index2] != target:
            index1 = -1
            index2 = -1
        return [index1, index2]


if __name__ == '__main__':
    solution = Solution()
    print solution.searchRange([0,1,1,1,2,2,4], 1)
