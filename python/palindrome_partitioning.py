#! /usr/bin/python

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
Additional quesiton:
Return the minimal cut for partition
'''


class Solution:
	# @param s, a string
	# @return boolean
	def palindrome(self, s):
		return s == s[::-1]

    # @param s, a string
    # @return a list of string
	def partition_recursive(self, output_list, a_list, s):
		if not s:
			output_list.append(a_list[:])
		for index in range(1, len(s) + 1):
			start_string = s[:index]
			if self.palindrome(start_string):
				a_list.append(start_string)
				self.partition_recursive(output_list, a_list, s[index:])
				a_list.pop()
	
	# @param s, a string
	# @return a list of lists of string
	def partition(self, s):
		if not s:
			return []
		output_list = list()
		self.partition_recursive(output_list, list(), s)
		return output_list

    # @param s, a string
    # @return an integer
	def minCut(self, s):
		# a easy solution is to first partition list and find the minimual length
		# but it is not time efficient

if __name__ == '__main__':
	solution = Solution()
	print solution.minCut('aaabaa')

