'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class Solution(object):
    def aux(self, nums):
        for denom in range(2, min(nums)+1):
            if all(num % denom == 0 for num in nums):
                return denom
        return 1

    def repeatedSubstringPattern(self, s):
        """
        :type str: s
        :rtype: bool
        """
        import collections
        size = len(s)
        if size < 2:
            return False
        freq = collections.Counter(s)
        denom = self.aux(freq.values())
        if denom == 1:
            return False
        sub_string = s[:size/denom]
        return sub_string * denom == s

solution = Solution()
print solution.repeatedSubstringPattern("abab")
print solution.repeatedSubstringPattern("ababab")
print solution.repeatedSubstringPattern("aba")
print solution.repeatedSubstringPattern("abaababaab")
