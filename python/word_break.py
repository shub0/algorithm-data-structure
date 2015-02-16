#! /usr/bin/python

'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return False
        segment_length = set()
        segment_length.add(0)
        for index in range(len(s)):
            for success_index in segment_length:
                if s[success_index:index + 1] in dict:
                    segment_length.add(index + 1)
                    break
        for length in segment_length:
            print length
        return ((len(s)) in segment_length)
    
if __name__ == '__main__':
    solution = Solution()
    print solution.wordBreak('leetcode', ['leet', 'code'])
