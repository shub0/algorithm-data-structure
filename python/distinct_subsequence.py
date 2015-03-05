#! /usr/bin/python

'''
 Given a string S and a string T, count the number of distinct subsequences of T in S.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
Here is an example:
S = "rabbbit", T = "rabbit"
Return 3. 
'''

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
		size_s = len(S)
		size_t = len(T)
		if size_s * size_t == 0:
			return 0
		dp_array = [ [0] * size_s for index in range(size_t) ]
		dp_array[0][0] = 1 if S[0] == T[0] else 0
		for index in range(1, size_s):
			if S[index] == T[0]:
				dp_array[0][index] = dp_array[0][index - 1] + 1
			else:
				dp_array[0][index] = dp_array[0][index - 1]
		for index_s in range(1, size_s):
			for index_t in range(1, size_t):
				if S[index_s] == T[index_t]:
					dp_array[index_t][index_s] = dp_array[index_t][index_s - 1] + dp_array[index_t - 1][index_s - 1]
				else:
					dp_array[index_t][index_s] = dp_array[index_t][index_s - 1]
		return dp_array[size_t-1][size_s-1]

if __name__ == '__main__':
	solution = Solution()
	print solution.numDistinct('rabbbit', 'rabbit')

			
