#! /usr/bin/python

'''
 Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
		size1 = len(word1)
		size2 = len(word2)
		if size1 == 0:
			return size2
		elif size2 == 0:
			return size1
		dp_array = [ [0] * (size2 + 1) for index in range(size1 + 1) ]
		dp_array[0][0] = 0 if word1[0] == word2[0] else 1
		for index in range(size1 + 1):
			dp_array[index][0] = index
		for index in range(size2 + 1):
			dp_array[0][index] = index
		for index1 in range(1, size1+1):
			for index2 in range(1, size2+1):
				if word1[index1 - 1] == word2[index2 - 1]:
					dp_array[index1][index2] = dp_array[index1-1][index2-1]
				else:
					dp_array[index1][index2] = min([dp_array[index1-1][index2-1], dp_array[index1-1][index2], dp_array[index1][index2-1]]) + 1
		return dp_array[-1][-1]

if __name__ == '__main__':
	solution = Solution()
	print solution.minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically")
