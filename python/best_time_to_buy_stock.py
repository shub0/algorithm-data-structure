'''
Say you have an array for which the ith element is the price of a given stock on day i.

1. If you were only permitted to complete at most one transaction
2. You may complete as many transactions as you like
3. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):

   def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        MAX_INT = 1e10
        size = len(prices)
        profit = 0
        min_price = MAX_INT
        for index in range(size):
            min_price = min(min_price, prices[index])
            profit = max(profit, prices[index] - min_price)
        return profit

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        MAX_INT = 1e10
        profit = 0
        buy_price = MAX_INT
        for index in range(size):
            if prices[index] >=  buy_price:
                profit += (prices[index] - buy_price)
                buy_price = MAX_INT
            if (index < size - 1) and (prices[index+1] > prices[index]):
                buy_price = prices[index]
        return profit

        def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        MIN_INT = -1e10
        buy1, buy2 = MIN_INT, MIN_INT
        profit1, profit2 = 0, 0
        for price in prices:
            buy1 = max(buy1, -price)
            profit1 = max(profit1, price+buy1)
            buy2 = max(buy2, profit1-price)
            profit2 = max(profit2, price+buy2)
        return profit2
