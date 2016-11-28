'''
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        import collections
        size = len(s)
        if len(s) < k:
            return k
        start, end = 0, 0
        max_count, max_size = 0, 0
        freq = collections.defaultdict(int)
        while end < size:
            freq[s[end]] += 1
            max_count = max(max_count, freq[s[end]])
            while (end - start + 1 - max_count > k):
                freq[s[start]] -= 1
                start += 1
            max_size = max(max_size, end - start + 1)
            end += 1
        return max_size

solution = Solution()
print solution.characterReplacement("AABABBA", 1)
print solution.characterReplacement("ABAB", 2)
