#! /usr/bin/python

'''
 Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution:
    MAX_INT = 2147483647
    MIN_INT = -2147483648
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        sign = 1
        if (dividend > 0) is not (divisor > 0):
            sign = -1
        if divisor == 0:
            return Solution.MAX_INT if sign > 0 else Solution.MIN_INT
        dividend, divisor, count, result = abs(dividend), abs(divisor), 0, 0
        while dividend >= divisor:
            divisor <<= 1
            count   += 1
        if count > 0:
            divisor >>= 1
            count   -= 1

        while count >= 0:
            if dividend >= divisor:
                result += (1 << count)
                dividend -= divisor
            divisor >>= 1
            count -= 1

        result *= sign

        if result >= Solution.MAX_INT:
            return Solution.MAX_INT
        if result <= Solution.MIN_INT:
            return Solution.MIN_INT
        return result

if __name__ == '__main__':
    solution = Solution()
    print solution.divide(110, 1)
