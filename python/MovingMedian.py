"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].
"""


import heapq
import collections

class Median(object):
    def __init__(self, nums):
        self.k = len(nums)
        self.low = list()      # max heap
        self.high = list()     # min heap
        for num in nums:
            heapq.heappush(self.low, (-num, num))
        for index in range(self.k/2):
            _, num = heapq.heappop( self.low )
            heapq.heappush(self.high, (num, num))
        self.log = collections.defaultdict(int)
        self.balance = 0

    def remove(self, num):
        self.log[num] += 1
        self.balance = 0

        if self.low and num <= self.low[0][1]:
            self.balance -= 1
        else:
            self.balance += 1

    def add(self, num):
        if self.low and num <= self.low[0][1]:
            self.balance += 1
            heapq.heappush(self.low, (-num, num))
        else:
            self.balance -= 1
            heapq.heappush(self.high, (num, num))
        self._rebalance()

    def _rebalance(self):
        if (self.balance < 0):
            _, num = heapq.heappop( self.high )
            heapq.heappush( self.low, (-num, num) )
            self.balance += 1

        if (self.balance > 0):
            _, num = heapq.heappop( self.low )
            heapq.heappush( self.high, (num, num) )
            self.balance -= 1

        while (self.low and self.log[self.low[0][1]] > 0):
            _, num = heapq.heappop( self.low )
            self.log[num] -= 1

        while ( self.high and self.log[self.high[0][1]] > 0):
            _, num = heapq.heappop( self.high )
            self.log[num] -= 1

    def get(self):
        print map(lambda x: x[1], self.high)
        if self.k % 2 == 1:
            if len(self.low) > len(self.high):
                return 1.0 * self.low[0][1]
            else:
                return 1.0 * self.high[0][1]
        else:
            return 0.5 * self.low[0][1] + 0.5 * self.high[0][1]

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        output = list()
        median = Median(nums[:k])
        size = len(nums)
        for (index) in range(k, size):
            output.append(median.get())
            median.remove(nums[index-k])
            median.add(nums[index])
        output.append(median.get())
        return output

solution = Solution()
print solution.medianSlidingWindow([7,8,8,3,8,1,5,3,5,4], 3)
