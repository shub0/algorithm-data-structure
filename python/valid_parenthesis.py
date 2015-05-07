#! /usr/bin/python

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    def match(self, char_1, char_2):
        if char_1 == '(' and char_2 == ')':
            return True
        if char_1 == '[' and char_2 == ']':
            return True
        if char_1 == '{' and char_2 == '}':
            return True
        return False

    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = list()
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_char = stack.pop()
                if not self.match(last_char, char):
                    return False
        return len(stack) == 0

if __name__ == '__main__':
    solution = Solution()
    print solution.isValid('()[{)]{}')
