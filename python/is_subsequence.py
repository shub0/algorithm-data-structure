'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_size = len(t)
        index = 0
        for char in s:
            while index < t_size and t[index] != char:
                index += 1
            if index == t_size:
                return False
            index += 1
        return True

    def isSubsequence2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        import bisect
        idxes = collections.defaultdict(list)
        for (index, char) in enumerate(t):
            idxes[char].append(index)
        curr = -1
        for char in s:
            locs = idxes.get(char, [])
            idx = bisect.bisect(locs, curr)
            if idx == len(locs):
                return False
            curr = locs[idx]
        return True


solution = Solution()
print solution.isSubsequence("axc", "abhgdc")
print solution.isSubsequence("ahc", "abhgdc")
print solution.isSubsequence("aab", "acbdaehdb")
print solution.isSubsequence("acb", "ahbgdc")
