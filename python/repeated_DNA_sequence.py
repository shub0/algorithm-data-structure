#! /usr/bin/python

'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the 
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        sequence_set = set()
        repeated_sequence = set()
        N = 10
        for index in range(0, len(s) - N + 1):
            sub_sequence = s[index:index+N]
            if sub_sequence in sequence_set:
                repeated_sequence.add(sub_sequence)
            else:
                sequence_set.add(sub_sequence)
        return list(repeated_sequence)

if __name__ == '__main__':
    solution = Solution()
    print solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
