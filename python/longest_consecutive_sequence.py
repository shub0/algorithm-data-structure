#! /usr/bin/python

'''
 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity. 
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
		visited = { x: False for x in num }
		max_len = 1
		for x in visited:
			if visited[x]:
				continue
			next = x+1
			right_len = 0
			while next in visited:
				right_len += 1
				visited[next] = True
				next += 1
			prev = x-1
			left_len = 0
			while prev in visited:
				left_len += 1
				visited[prev] = True
				prev -= 1
			max_len = max(max_len, left_len + right_len + 1)
		return max_len

if __name__ == '__main__':
	solution = Solution()
	print solution.longestConsecutive([1,3,2,4,5])
