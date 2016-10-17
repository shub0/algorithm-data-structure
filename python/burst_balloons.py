'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 <= n <= 500, 0 <= nums[i] <= 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''

class Solution(object):
    def maxCoins(self, iNums):
        """
        :type iNums: List[int]
        :rtype: int
        """
        nums = [1] + [num for num in iNums if num > 0] + [1]
        size = len(nums)
        dp_array = [ [0] * size for _ in range(size) ]
        for k in range(2, size):
            for left in range(0, size - k):
                right = left + k
                for i in range(left+1, right):
                    dp_array[left][right] = max(dp_array[left][right], nums[left] * nums[i] * nums[right] + dp_array[i][right] + dp_array[left][i])

        return dp_array[0][size-1]

solution = Solution()
print solution.maxCoins([3,1,5,8])
