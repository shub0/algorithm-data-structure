#! /usr/bin/python

'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
    The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

class Solution:
    def kSum(self, num, k, target):
        output = set()
        index1 = 0
        if k == 2:
            index2 = len(num) - 1
            while index1 < index2:
                if num[index1] + num[index2] == target:
                    output.add((num[index1], num[index2]))
                    index1 += 1
                elif num[index1] + num[index2] > target:
                    index2 -= 1
                else:
                    index1 += 1
        else:
            while index1 < len(num) - k + 1:
                new_target = target - num[index1]
                sub_set = self.kSum(num[index1+1:], k - 1, new_target)
                if sub_set:
                    output.update(set( (num[index1],) + solution for solution in sub_set ))
                index1 += 1
        return output
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        output = self.kSum(num, 4, target)
        return [ list(solution)  for solution in output ]

if __name__ == '__main__':
    solution = Solution()
    print solution.fourSum([1,0,-1,0,-2,2], 0)
