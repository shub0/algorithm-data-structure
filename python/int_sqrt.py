#! /usr/bin/python

class Solution:
    # @param x, an integer
    # @return an integer
	def sqrt_newton(self, x):
		if x < 0:
			raise ValueError('non-negative number only')
		if x == 0:
			return 0
		MAX_COUNT = 20
		_x = x * 1.0
		root = x * 1.0
		for index in range(MAX_COUNT):
			root = (root + _x / root) / 2.0
		return int(root)

	# @param x, an integer
	# @return an integer
	def sqrt(self, x):
		if x < 0:
			raise ValueError
		if x == 0:
			return 0
		# coarse search
		coarse_root = 1
		GRADIENT = 10
		while (coarse_root * coarse_root < x):
			coarse_root *= GRADIENT
		for root in range(coarse_root / GRADIENT, coarse_root):
			if (root * root > x):
				break
		return root - 1
if __name__ == '__main__':
	solution = Solution()
	print solution.sqrt(1579205274)
