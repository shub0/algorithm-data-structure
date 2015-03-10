#! /usr/bin/python

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
		if n < 3:
			return n
		dp_array = [0] * n
		dp_array[0] = 1
		dp_array[1] = 2
		for index in range(3, n):
			dp_array[index] = dp_array[index - 1] + dp_array[index - 2]
		return dp_array[-1]


