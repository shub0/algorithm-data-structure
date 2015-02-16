#! /usr/bin/python
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    # You may assume no duplicate exists in the array.
    def findMinNoDuplicate(self, num):
        INT_MIN_VALUE = -(2**32)
        size = len(num)
        if size == 0:
            return INT_MIN_VALUE
        elif size == 1:
            return num[0]
        low_index = 0
        high_index = size - 1
        while (low_index < high_index - 1):
            mid_index = low_index + (high_index - low_index) / 2
            if (num[mid_index] > num[high_index]):
                low_index = mid_index
            else:
                high_index = mid_index
        return min(num[low_index], num[high_index])

    # @param num, a list of integer
    # @return an integer
    # You may assume duplicate exists in the array.
    def findMinDuplicate(self, num):
        INT_MIN_VALUE = -(2**32)
        size = len(num)
        if size == 0:
            return INT_MIN_VALUE
        elif size == 1:
            return num[0]
        low_index = 0
        high_index = size - 1
        while (low_index < high_index - 1):
            mid_index = low_index + (high_index - low_index) / 2
            if (num[mid_index] > num[high_index]):
                low_index = mid_index
            elif (num[mid_index] < num[high_index]):
                high_index = mid_index
            else:
                high_index -= 1
        return min(num[low_index], num[high_index])

if __name__ == '__main__':
    solution = Solution()
    print solution.findMinDuplicate([3,3,1,2,2])
