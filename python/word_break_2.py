#! /usr/bin/python

'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"]
'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, word_dict):
        if len(s) == 0:
            return list()
        segments = ['']
        for index in range(len(s)):
            new_segments = []
            for segment in segments:
                segment_length = sum([len(x) for x in segment.split()])
                if s[segment_length:index+1] in word_dict:
                    new_segment = '%s %s' % (segment, s[segment_length:index+1])
                    new_segments.append(new_segment)
            segments.extend(new_segments)
        solution_list = list()
        for segment in segments:
            if sum([len(x) for x in segment.split()]) == len(s):
                   solution_list.append(segment.strip())
        return solution_list

if __name__ == '__main__':
    solution = Solution()
    print solution.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
