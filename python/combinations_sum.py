#! /usr/bin/python

'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSumShort(self, candidates, target):
        output = []
        candidates.sort()
        for index in range(len(candidates)):
            num = candidates[index]
            if target > num:
                sub_output = self.combinationSum(candidates[index:], target -  num)
                if len(sub_output) > 0:
                    output += [ [num] + a_list for a_list in sub_output ]
            elif target == num:
                output += [ [num] ]
            else:
                break
        return output

    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        output = []
        size = len(candidates)
        if size == 0:
            return output
        candidates.sort()
        self.make_combination(candidates, target, 0, list(), output)
        return output

    def make_combination(self, candidates, target,start_index, a_list, output):
        if target == 0:
            output.append(a_list[:])
        else:
            size = len(candidates)
            for index in range(start_index, size):
                if target < candidates[index]:
                    break
                a_list.append(candidates[index])
                self.make_combination(candidates, target - candidates[index], index, a_list, output)
                a_list.pop()

if __name__ == '__main__':
    solution = Solution()
    print solution.combinationSum([48,22,49,24,26,47,33,40,37,39,31,46,36,43,45,34,28,20,29,25,41,32,23], 69)
