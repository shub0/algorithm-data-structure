'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
'''

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        if n % 3 == 1:
            power2 = 2
            n -= 4
        elif n % 3 == 2:
            power2 = 1
            n -= 2
        else:
            power2 = 0
        power3 = n / 3
        return (3 ** power3) * (2 ** power2)
