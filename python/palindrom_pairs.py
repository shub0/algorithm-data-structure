'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_dict = { word: i for i, word in enumerate(words) }
        output = list()
        for word_index in range(len(words)):
            word = words[word_index]
            for index in range(len(word)+1):
                segment = word[:index]
                reverse_segment = segment[::-1]
                left = word[index:]
                reverse_left = left[::-1]
                if reverse_segment in word_dict and word_dict[reverse_segment] != word_index and left == reverse_left:
                    output.append( [word_index, word_dict[reverse_segment]] )
                if index != 0 and reverse_left in word_dict and word_dict[reverse_left] != word_index and segment == segment[::-1]:
                    output.append( [word_dict[reverse_left], word_index] )
        return output

solution = Solution()
print solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
