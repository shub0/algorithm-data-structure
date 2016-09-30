#! /usr/bin/python

'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
cd p
Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"]
'''

class Solution(object):
    def check(self, s, wordDict):
        size = len(s)
        dp = [False for i in range(size+1)]
        dp[0] = True
        for i in range(1, size+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[size]

    def dfs(self, s, wordDict, string):
        if self.check(s, wordDict):
            if len(s) == 0:
                self.output.append(string[1:])
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, string+' '+s[:i])

    def wordBreak(self, s, wordDict):
        self.output = list()
        self.dfs(s, wordDict, '')
        return self.output


if __name__ == '__main__':
    solution = Solution()
    print solution.wordBreak('catsanddogdog', ["cat", "cats","an", "and", "sand", "dog"])
