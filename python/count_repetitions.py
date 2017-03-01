"""
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] = "abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, "abc" can be obtained from "abdbec" based on our definition, but it can not be obtained from "acbbe".

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 <= n1 <= 10^6 and 1 <= n2 <= 10^6. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.
"""

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if not s2 or not s1 or n1 * n2 == 0:
            return 0
        M, c1, c2, l1, l2 = 0, 0, 0, len(s1), len(s2)
        for c1 in range(l1 * n1):
            if c2 == l2 * n2:
                break
            if s2[c2 % l2] == s1[c1 % l1]:
                c2 += 1
        print c1, c2
        if c2 == n2 * l2:
            return (1.0 * l1 * n1 ) / c1
        return 0

solution = Solution()
print solution.getMaxRepetitions("niconiconi", 99981, "nico", 81)
