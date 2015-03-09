#! /usr/bin/python

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
For example,
If n = 4 and k = 2, a solution is:
[
  [2,4], [3,4], [2,3], [1,2], [1,3], [1,4]
]
'''

class Solution:
    def __init__(self):
        self.combine_list = list()
    # @return a list of lists of integers
    def combine(self, n, k):
        if k == 0 or n == 0 or k > n:
            return []
        else:
            a_list = list()
            self.combine_recursive(1, k, n, a_list)
            return self.combine_list
    
    # @param n an integer
    # @param k an integer
    # @param N an integer
    # @param combine_list a list of lists of integers
    def combine_recursive(self, n, k, N, a_list):
        if len(a_list) == k: 
            self.combine_list.append(a_list)
        elif n > N:
            return
        else:
            size = len(a_list)
            a_list.append(n)
            self.combine_recursive(n+1, k, N, a_list)
            a_list = a_list[:size]
            self.combine_recursive(n+1, k, N, a_list)
    
    def combine_no_recursive(self, n, k):
        if k == 0 or k > n:
            return []
        combine_list = [[]]
        for index in range(1, n+1):
            combine_list.extend( [ a_list + [index] for a_list in filter(lambda x: len(x) < k, combine_list) ] )
        return filter(lambda x: len(x) == k, combine_list)

if __name__ == '__main__':
    solution = Solution()
    print solution.combine_no_recursive(4,2)
