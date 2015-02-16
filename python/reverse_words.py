#! /usr/bin/pyhon

'''
Given an input string, reverse the string word by word.
For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    solution = Solution()
    print solution.reverseWords('the sky is blue')
