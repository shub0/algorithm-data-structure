#! /usr/bin/python

'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        size = len(s)
        if size < 2:
            return 0
        max_len = 0
        count = 0
        result = 0
        marker = list(s)
        for index in range(size):
            if marker[index] == '(':
                count += 1
            elif count > 0:
                count -= 1
            else:
                count = 0
                marker[index] = '*'
        count = 0
        for index in range(size - 1, -1, -1):
            if marker[index] == '*':
                max_len = max(max_len, result)
                result = 0
                count = 0
            elif marker[index] == ')':
                count += 1
            else:
                if count > 0:
                    result += 1
                    count -= 1
                else:
                    max_len = max(max_len, result)
                    result = 0
                    count = 0
        max_len = max(max_len, result)
        print marker
        return 2 * max_len

if __name__ == '__main__':
    solution = Solution()
    print solution.longestValidParentheses(')()())')
