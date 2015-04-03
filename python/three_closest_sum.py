#! /usr/bin/python

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        import math
        _num = sorted(num)
        INT_MAX = 1e9
        min_sum = INT_MAX
        size = len(num)
        for index1 in range(size - 2):
            index2 = index1 + 1
            index3 = size - 1
            while index2 < index3:
                curr_sum = _num[index1] + _num[index2] + _num[index3] - target
                if curr_sum > 0:
                    index3 -= 1
                elif curr_sum < 0:
                    index2 += 1
                else:
                    return target
                if math.fabs(min_sum) > math.fabs(curr_sum):
                    min_sum = curr_sum
        return min_sum + target


if __name__ == '__main__':
    solution = Solution()
    print solution.threeSumClosest([-1,2,-1,4], 1)
    print solution.threeSumClosest([1,1,1,0], 100)
