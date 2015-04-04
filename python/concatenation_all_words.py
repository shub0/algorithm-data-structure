#! /usr/bin/python

'''
 You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution:
    def segmentMatch(self, word_size, word_dict, S):
        import collections
        index = 0
        curr_dict = collections.defaultdict(int)
        while index < len(S):
            curr_word = S[index:index+word_size]
            if curr_word not in word_dict:
                return False
            index += word_size
            curr_dict[curr_word] += 1
        for word in word_dict:
            if word not in curr_dict or curr_dict[word] != word_dict[word]:
                return False
        return True

    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        import collections
        dict_size = len(L)
        word_size = len(L[0])
        str_size  = len(S)
        output    = list()
        word_dict = collections.defaultdict(int)
        if str_size < dict_size * word_size:
            return output
        for word in L:
            word_dict[word] += 1
        index = 0
        while index < str_size:
            if self.segmentMatch(word_size, word_dict, S[index:index+dict_size*word_size]):
                output.append(index)
            index += 1
         return output

if __name__ == '__main__':
    solution = Solution()
    print solution.findSubstring('barfoothefoobarman', ['foo', 'bar'])
    print solution.findSubstring('aaa', ['a','a'])
