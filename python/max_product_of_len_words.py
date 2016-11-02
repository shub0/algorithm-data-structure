'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def signature(word):
            sign = 0
            for char in set(word):
                sign |= (1 << (ord(char) - 97))
            return sign
        signs = {word: signature(word) for word in words}
        size = [ len(w1)*len(w2)  for w1 in signs for w2 in signs if not signs[w1] & signs[w2] ]
        if len(size) > 0:
            return max(size)
        return 0

solution = Solution()
print solution.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
print solution.maxProduct( ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
print solution.maxProduct(["a", "aa", "aaa"])
