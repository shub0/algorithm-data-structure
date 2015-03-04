#! /usr/bin/python

'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        size = len(ratings)
        if size < 2:
            return size
        candy = [0] * size
        candy[0] = 1
        for index in range(1, size):
            if ratings[index] > ratings[index - 1]:
                candy[index] = candy[index - 1] + 1
            else:
                candy[index] = 1
        for index in range(size - 2, -1, -1):
            if ratings[index] > ratings[index + 1] and candy[index] <= candy[index + 1]:
                candy[index] = candy[index + 1] + 1
        print candy
        return sum(candy)

if __name__ == '__main__':
    solution = Solution()
    print solution.candy([1,2,2])
