#! /usr/bin/python

'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        size = len(digits)
        carry_on = 1
        for index in range(size - 1, -1, -1):
            sum = digits[index] + carry_on
            carry_on = sum / 10
            digits[index] = sum % 10
            if carry_on == 0:
                break
        if carry_on == 1:
            digits.insert(0,1)
        return digits

if __name__ == '__main__':
    solution = Solution()
    print solution.plusOne([9,9,9])
    print solution.plusOne([0])
    print solution.plusOne([])
    print solution.plusOne([9,8,9])

