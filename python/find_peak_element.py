#! /usr/bin/python

'''
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

class Solution(object):
    def findPeakElement(self, num):
        '''
        1. at peak
        2. at valley
        3. at increasing slope
        4. at decreasing slope
        '''
        size = len(num)
        if (size == 0): return -1
        if (size == 1): return 0
        low_index = 0
        high_index = size - 1
        while(low_index < high_index - 1):
            mid_index = low_index + (high_index - low_index) / 2
            # case 1
            if ( num[mid_index] > num[mid_index - 1] and num[mid_index] > num[mid_index+1] ):
                return mid_index
            # case 4
            elif (num[mid_index] < num[mid_index-1]):
                high_index = mid_index
            # case 2 and 3
            # if case 2, we can search either direction
            else:
                low_index = mid_index
        if num[low_index] > num[high_index]:
            return low_index
        return high_index

if __name__ == '__main__':
    solution = Solution()
    print solution.findPeakElement_fast([1,2,3,3,3])
