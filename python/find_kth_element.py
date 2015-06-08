#! /usr/bin/python

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length.
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        import heapq
        heap = list()
        for ex in nums:
            heapq.heappush(heap, ex)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


if __name__ == '__main__':
    data = range(1, 11)
    solution = Solution()
    print data
    print solution.findKthLargest(data, 3)
