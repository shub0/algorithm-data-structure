'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
*
* *
* * *

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
*
* *
* * *
* *

Because the 4th row is incomplete, we return 3.

'''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        import bisect
        end = int(math.sqrt(2 * n) + 1)
        start = 0
        while start < end:
            mid = (end - start) / 2 + start
            curr_sum = mid * (mid+1) / 2
            next_sum = (mid+1) * (mid+2) / 2
            if curr_sum <= n and next_sum > n:
                return mid
            elif curr_sum > n:
                end = mid - 1
            else:
                start = mid + 1
        return start

solution = Solution()
print solution.arrangeCoins(8)
print solution.arrangeCoins(3)
print solution.arrangeCoins(100)
