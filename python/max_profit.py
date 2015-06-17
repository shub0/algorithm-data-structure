#! /usr/bin/python

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Problem 1:
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Problem 2:
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Problem 3:
Design an algorithm to find the maximum profit. You may complete at most two transactions.
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Problem 4:
Design an algorithm to find the maximum profit. You may complete at most k transactions.
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit1(self, prices):
        size = len(prices)
        if size < 2:
            return 0
        buy_price = prices[0]
        profit = 0
        for day_index in range(1, size):
            if prices[day_index] < buy_price:
                buy_price = prices[day_index]
            else:
                profit = max(profit, prices[day_index] - buy_price)
        return profit

    # @param prices, a list of integer
    # @return an integer
    def maxProfit2(self, prices):
        profit = 0
        for day_index in range(1, len(prices)):
            if (prices[day_index] > prices[day_index - 1]):
                profit += prices[day_index] - prices[day_index-1]
        return profit

    # @param prices, a list of integer
    # @return an integer
    def maxProfit3(self, prices):
        size = len(prices)
        if size < 2:
            return 0
        profit = [0] * size
        first_profit = 0
        # assume buy at the first day
        buy_price = prices[0]
        for day_index in range(1, size):
            if prices[day_index] < buy_price:
                # update buy price if lower than previous buy price
                buy_price = prices[day_index]
            else:
                # try to sell at day day_index
                first_profit = max(first_profit, prices[day_index] - buy_price)
            profit[day_index] += first_profit
        # assume sell at the last day
        sell_price = prices[size - 1]
        second_profit = 0
        for day_index in range(size - 2, -1, -1):
            # update sell price if better
            if prices[day_index] > sell_price:
                sell_price = prices[day_index]
            else:
                second_profit = max(second_profit, sell_price - prices[day_index])
            profit[day_index] += second_profit
        return max(profit)

if __name__ == '__main__':
    solution = Solution()
    print solution.maxProfit1([5,4,3,6,8,10,9,15])
    print solution.maxProfit2([5,4,3,6,8,10,9,15])
    print solution.maxProfit3([1,2,4,2,5,7,2,4,9,0])
