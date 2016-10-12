'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n < 4:
            return n
        count = [0] * n
        squares = [1]
        for num in range(1,n+1):
            k = int(math.sqrt(num))
            index = num - 1
            if k * k == num:
                count[index] = 1
                squares.append(num)
            else:
                count[index] = min([ count[index-square] for square in squares[:k+1] ]) + 1
        return count[-1]

solution = Solution()
print solution.numSquares(13)
print solution.numSquares(4)
print solution.numSquares(5)
print solution.numSquares(7115)
print solution.numSquares(8405)
