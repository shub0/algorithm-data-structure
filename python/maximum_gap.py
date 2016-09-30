#! /usr/bin/python

'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.
Return 0 if the array contains less than 2 elements.
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    # The solution is in fact a bucket sorting
    def maximumGap(self, num):
        size = len(num)
        if (size < 2):
            return 0
        min_value = min(num)
        max_value = max(num)
        bucket_size = (max_value - min_value) / (size) + 1
        bucket_min_max = [(float('inf'), float('-inf')) for index in range(size)]

        for element in num:
            index = (element - min_value) / bucket_size
            bucket_min_max[index] = (min(ucket_min_max[index][0], element), max(bucket_min_max[index][1], element))

        gap = 0
        last_max = bucket_min_max[0][1]
        for bucket_min, bucket_max in bucket_min_max[1:]:
            if bucket_min == float('inf'):
                continue
            gap = max(gap, bucket_min - last_max)
            last_max = bucket_max
        return gap

if __name__ == '__main__':
    solution = Solution()
    print solution.maximumGap([1,3,4,5,9])
