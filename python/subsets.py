#! /usr/bin/python

'''
Given a set of distinct integers, S, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If S = [1,2,3], a solution is:

[
  [3],  [1],  [2],  [1,2,3],  [1,3],  [2,3],  [1,2],  []
]

Extend:
Assume there are duplicates in the collection
'''


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
		size = len(S)
		if size == 0:
			return []
		sorted_s = sorted(S)
		result_list = [[]]
		for index in range(size):
			result_list.extend( [ prev_list+[sorted_s[index]] for prev_list in result_list ])
		return result_list

    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
		size = len(S)
		if size == 0:
			return []
		result_list = [[]]
		sorted_s = sorted(S)
		start_index = 0
		for index in range(size):
			if index == 0 or sorted_s[index] != sorted_s[index - 1]:
				start_index = len(result_list)
			result_list.extend([ prev_list+[sorted_s[index]] for prev_list in result_list[-start_index:] ])
		return result_list

if __name__ == '__main__':
	solution = Solution()
	print solution.subsets([1,2,3])
	print solution.subsetsWithDup([5,5,5,5,5,5])
