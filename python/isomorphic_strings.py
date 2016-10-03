'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        size_s = len(s)
        size_t = len(t)
        if (size_s != size_t):
            return False
        map = dict()
        for char_s, char_t in zip(s,t):
            if char_s not in map:
                map[char_s] = char_t
            elif map[char_s] != char_t:
                return False
        return len(set(map.values())) == len(map.keys())
