'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import collections
        w_hash = collections.defaultdict(int)
        p_hash = collections.defaultdict(int)
        for char in p:
            p_hash[char] += 1
        p_size = len(p)
        s_size = len(s)
        output = list()
        start = 0
        end = 0
        if s_size < p_size:
            return output
        while end < p_size:
            w_hash[s[end]] += 1
            end += 1
        while end < s_size:
            if w_hash == p_hash:
                output.append(start)
            w_hash[s[start]] -=1
            if w_hash[s[start]] == 0:
                del w_hash[s[start]]
            start += 1
            w_hash[s[end]] += 1
            end += 1
        if w_hash == p_hash:
            output.append(start)
        return output

solution = Solution()
print solution.findAnagrams("abab", "ab")
print solution.findAnagrams("cbaebabacd", "abc")
