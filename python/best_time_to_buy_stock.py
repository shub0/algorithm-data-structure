'''
Say you have an array for which the ith element is the price of a given stock on day i.

1. If you were only permitted to complete at most one transaction
2. You may complete as many transactions as you like
3. You may complete at most two transactions.
4. You may complete at most K transactions
5. You may complete as many as you want, but you must have at least one cool down after each sell.

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
        loan1, loan2 = MIN_INT, MIN_INT
        profit1, profit2 = 0, 0
        for price in prices:
            loan1 = max(loan1, -price)
            profit1 = max(profit1, price+loan1)
            loan2 = max(loan2, profit1-price)
            profit2 = max(profit2, price+loan2)
        return max(profit2, profit1)

    def maxProfit4(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k < 1:
            return 0
        if k >= len(prices) / 2:
            return self.maxProfit2(prices)

        MIN_INT = -1e10
        loan = [MIN_INT] * k
        profit = [0] * (k)
        for price in prices:
           for index in range(k):
               if index == 0:
                   loan[index] = max(loan[index], -price)
               else:
                   loan[index] = max(loan[index], profit[index-1] - price)
               profit[index] = max(profit[index], price+loan[index])
        return max(profit)

     def maxProfit5(self, prices):
        if len(prices) < 2:
           return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
           prev_buy = buy
           buy = max(prev_sell - price, prev_buy)
           prev_sell = sell
           sell = max(prev_buy + price, prev_sell)
         return sell
