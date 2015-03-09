#! /usr/bin/python

'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
'''

# The code does not pass OJ test cases due to the limiation of LeetCode
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        gray_code = []
        if n == 0:
            return []
        gray_code = []
        for index in range(1, n+1):
            if index == 1:
                gray_code.extend(['0', '1'])
                continue
            prev_code = gray_code
            gray_code = []
            gray_code.extend([ code + '0' for code in prev_code ])
            gray_code.extend([ code + '1' for code in prev_code[::-1] ])
        return [ int(code, 2) for code in gray_code ]

if __name__ == '__main__':
    solution = Solution()
    print solution.grayCode(2)
