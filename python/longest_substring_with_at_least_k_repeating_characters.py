'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        import collections
        if len(s) < k:
            return 0
        idxes = collections.defaultdict(list)
        for (index, char) in enumerate(s):
            idxes[char].append(index)
        segment_idx = []
        for (char, locs) in idxes.items():
            if len(locs) < k:
                segment_idx += locs
        if len(segment_idx) == 0:
            return len(s)
        segment_idx.sort()
        segment_idx.append(len(s))
        start = 0
        max_size = 0
        for end in segment_idx:
            max_size = max(max_size, self.longestSubstring(s[start:end], k))
            start = end + 1
        return max_size

    def longestSubstring2(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


solution = Solution()
print solution.longestSubstring("aaabbc", 2)
print solution.longestSubstring("aaabb", 3)
print solution.longestSubstring("bbaaacbd", 3)

