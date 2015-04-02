#! /usr/bin/python

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        _num = sorted(num)
        size = len(num)
        solution = set()
        first = 0
        for first in range(size - 2):
            second = first + 1
            last   = size - 1
            while (second < last):
                sum = _num[first] + _num[second] + _num[last]
                if sum > 0:
                    last -= 1
                elif sum < 0:
                    second += 1
                else:
                    solution.add((_num[first], _num[second], _num[last]))
                    second += 1
        
        return [ list(triple) for triple in solution ]

if __name__ == '__main__':
    solution = Solution()
    print solution.threeSum([-1,0,1,2,-1,4,-1])
