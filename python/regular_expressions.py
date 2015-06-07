#! /usr/bin/python

'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a")         false
isMatch("aa","aa")        true
isMatch("aaa","aa")  	  false
isMatch("aa", "a*")       true
isMatch("aa", ".*")       true
isMatch("ab", ".*")       true
isMatch("aab", "c*a*b")   true
'''

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not s and not p:
            return True
        if not p and s:
            return False

        if p[-1] == '*':
            rep = p[-2]
            if s and (s[-1] == rep or rep == '.'):
                return self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2])
            else:
                return self.isMatch(s, p[:-2])
        else:
            if s and (s[-1] == p[-1] or p[-1] == '.'):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False

if __name__ == '__main__':
    solution = Solution()
    print solution.isMatch('aab', 'c*a*b')
