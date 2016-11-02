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

    def findKthElement(self, nums, k):
        size = len(nums)
        k = size - k + 1
        if size < k:
            raise ValueError("size of list(%d) is smaller than k(%d)" % (size, k))
        start = 0
        end = size - 1
        while True:
            pivot = nums[start]
            pivot_index = start
            for index in range(start, end+1):
                if nums[index] < pivot:
                    pivot_index += 1
                    nums[index], nums[pivot_index] = nums[pivot_index], nums[index]
            nums[start], nums[pivot_index] = nums[pivot_index], nums[start]

            left_size = pivot_index - start + 1
            # search first half
            if left_size > k:
                end = pivot_index
            # search second half
            elif left_size < k:
                start = pivot_index + 1
                k -= left_size
            else:
                return nums[pivot_index]

if __name__ == '__main__':
    import random
    data = range(1, 11)
    random.shuffle(data)
    solution = Solution()
    sort = sorted(data)
    k = 4
    print "Expected %d, got" % (sort[-k])
    print solution.findKthElement(data, k)
