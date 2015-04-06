#! /usr/bin/python

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, num, target):
        start = 0
        end   = len(num) - 1
        pos   = len(num)
        while start <= end:
            middle = (end - start) / 2 + start
            if target > num[middle]:
                start = middle + 1
            else:
                pos = middle
                end = middle - 1
        return pos


if __name__ == '__main__':
    solution = Solution()
    print solution.searchInsert([3,4,5,6,8,9], 7)
        
