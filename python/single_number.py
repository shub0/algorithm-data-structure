#! /usr/bin/python

'''
Question 1:
Given an array of integers, every element appears twice except for one. Find that single one.
Question 2:
Given an array of integers, every element appears three times except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

import operator
class Solution:
    # @param numbers, a list of integer
    # @return an integer
    def singleNumber(self, numbers):
        return reduce(lambda x, y: x^y, numbers)

    # @param numbers, a list of integer
    # @return an integer
    def singleNumber2(self, numbers):
        one = 0
        second = 0
        for num in numbers:
            one = (one ^ num) & ~second
            second = (second ^ num) & ~one
        return one

if __name__ == '__main__':
    solution = Solution()
    print solution.singleNumber([1,2,1])
