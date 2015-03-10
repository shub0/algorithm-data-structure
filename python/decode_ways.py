#! /usr/bin/python

'''
 A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2. 
'''

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
		size = len(s)
		if size == 0 or int(s[0]) == 0:
			return 0
		dp_array = [0] * size
		dp_array[0] = 1
		for index in range(1, size):
			if int(s[index]) > 0:
				dp_array[index] = dp_array[index - 1]
			num = int(s[index-1:index+1])
			if num > 9 and num < 27:
				if index > 1:
					dp_array[index] += dp_array[index-2]
				else:
					dp_array[index] += 1
			if dp_array[index] == 0:
				return 0
		return dp_array[-1]

if __name__ == '__main__':
	solution = Solution()
	print solution.numDecodings('126')
