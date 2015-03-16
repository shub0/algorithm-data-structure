#! /usr/bin/python

'''
Problem:
Given a collection of numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

Problem 2:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution:
    def __init__(self):
        self.result_list = list()

    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        size = len(num)
        num.sort()
        if size > 0:
            used = [False] * size
            self.make_permute(num, used, list())
        return self.result_list
        
    # @param num, a list of integer
    # @param used, a list of boolean
    # @param a_list, a list of integer
    def make_permute(self, num, used, a_list):
        if (len(a_list) == len(num)):
            self.result_list.append(a_list)
            return
        for index in range(len(num)):
            if not used[index]:
                if index > 0 and num[index] == num[index-1] and not used[index-1]:
                    continue
                used[index] = True
                list_size = len(a_list)
                a_list.append(num[index])
                self.make_permute(num, used, a_list)
                a_list = a_list[:list_size]
                used[index] = False

if __name__ == '__main__':
    solution = Solution()
    print len(solution.permute([1,2,3,4]))

            
        
