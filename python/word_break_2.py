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
        match_segments = list()
        if (s[0] in word_dict):
            match_segments.append([s[0]])
        else:
            match_segments.append([''])
        max_word_length = 0
        for word in word_dict:
            max_word_length = max(max_word_length, len(word))
        for index in range(1,len(s)):
            match_segments.append(list())
            for match_length in range(index - max_word_length, index):
                unmatch_segment = s[match_length:index+1]
                if unmatch_segment in word_dict:
                    if match_length == 0:
                        match_segments[index].append(unmatch_segment)
                        continue
                    for match_segment in match_segments[match_length-1]:
                        new_match_segment = '%s %s' % (match_segment, unmatch_segment)
                        match_segments[index].append(new_match_segment)
        
        return match_segments[len(s)-1]

    def wordBreak2(self, s, dict):
        self.dict = dict
        self.cache = {}
        return self.break_helper(s)

    def break_helper(self, s):
        combs = []
        if s in self.cache:
            return self.cache[s]
        if len(s) == 0:
            return []

        for i in range(len(s)):
            if s[:i+1] in self.dict:
                if i == len(s) - 1:
                    combs.append(s[:i+1])
                else:
                    sub_combs = self.break_helper(s[i+1:])
                    for sub_comb in sub_combs:
                        combs.append(s[:i+1] + ' ' + sub_comb)

        self.cache[s] = combs
        return combs

if __name__ == '__main__':
    solution = Solution()
    print solution.wordBreak2('catsanddogdog', ["cat", "cats","an", "and", "sand", "dog"])
