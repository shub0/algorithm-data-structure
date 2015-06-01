#! /usr/bin/python

'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        base = 1
        while x / base >= 10:
            base *= 10
        while x > 0:
            high_digit = x / base
            low_digit  = x % 10
            if high_digit != low_digit:
                return False
            x %= base # remove high digit
            x /= 10   # remove low digit
            base /= 100
        return True

if __name__ == '__main__':
    solution = Solution()
    print solution.isPalindrome(11011)
