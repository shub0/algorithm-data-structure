'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        import heapq
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
        sort_freq = [ (val, key) for key, val in freq.items() ]
        sort_freq.sort(key = lambda x: x[0], reverse=True)
        return map(lambda x: x[1], sort_freq[:k])
