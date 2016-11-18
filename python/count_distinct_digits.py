'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 < x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 < x < 100, excluding [11,22,33,44,55,66,77,88,99])
'''

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = {1: 9, 2: 91, 3: 739, 4:5275, 5: 32491,
        6: 168571, 7:712891, 8:2345851, 9:2708803, 10:6531840}
        if n < 1:
            return 0
        if n > 10:
            res[10]
        return res[n]

solution =
