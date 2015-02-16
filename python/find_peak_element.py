#! /usr/bin/python

'''
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    # simple solution is O(N)
    def findPeakElement_simple(self, num):
        size = len(num)
        if (size == 0): return -1
        if (size == 1): return 0
        for index in range(1, size - 1):
            if (num[index] > num[index - 1] and num[index] > num[index + 1]):
                return index
        if num[0] > num[1]: return 0
        if num[size - 1] > num[size - 2]: return size - 1
        return -1
class Solution:
    # @param num, a list of integer
    # @return an integer
    # Best solution is O(logN)
    # Following solution is not exactly what the quesiton requires
    def findPeakElement_fast(self, num):
        size = len(num)
        if (size == 0): return -1
        if (size == 1): return 0
        low_index = 0
        high_index = size - 1
        while(low_index < high_index):
            mid_index = low_index + (high_index - low_index) / 2
            if (num[mid_index] > num[mid_index + 1]):
                high_index = mid_index
            elif(num[mid_index] <= num[mid_index + 1]):
                low_index = mid_index + 1
        return low_index

if __name__ == '__main__':
    solution = Solution()
    print solution.findPeakElement_fast([1,2,3,3,3])
