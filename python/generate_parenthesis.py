#! /usr/bin/python

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
    def validParenthesis(self, string):
        check = 0
        for char in string:
            if char == '(':
                check += 1
                continue
            check -= 1
            if check < 0:
                return False
        return check == 0

    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n < 1:
            return set()
        string_dict = {'(': 1}
        for index in range(1, 2 * n):
            current_dict = dict()
            for string in string_dict.keys():
                check_num = string_dict[string]
                current_dict[string+'('] = check_num + 1
                if check_num > 0:
                    current_dict[string+')'] = check_num - 1
            string_dict = current_dict
        return filter(self.validParenthesis, string_dict.keys())

if __name__ == '__main__':
    solution  = Solution()
    print solution.generateParenthesis(4)
