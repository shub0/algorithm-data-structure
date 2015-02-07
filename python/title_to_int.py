#! /usr/bin/python

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
