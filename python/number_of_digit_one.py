'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_ones = 0
        base = 1
        while base <= n:
            r = n / base
            k = n % base
            num_ones += (r + 8) / 10 * base + (r % 10 == 1) * (k + 1)
            base *= 10
        return num_ones
