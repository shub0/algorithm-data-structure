'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        import sys
        num = [sys.maxint] * (amount + 1)
        num[0] = 0
        for index in range(amount + 1):
            for coin in coins:
                if index >= coin:
                    num[index] = min(num[index], num[index-coin] + 1)
        return num[-1] if num[-1] < sys.maxint else -1


solution = Solution()
print solution.coinChange([1,2,5],11)
print solution.coinChange([2], 3)
