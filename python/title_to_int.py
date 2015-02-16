#! /usr/bin/python

'''
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        N = 26
        result = 0
        for element in s:
            result *= N
            result += ord(element) - 64
        return result

if __name__ == '__main__':
    solution = Solution()
    print solution.titleToNumber('AA')
