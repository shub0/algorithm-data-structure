#! /usr/bin/python

'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
'''

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        if len(A) != m + n:
            return
        index_merged_array = m + n - 1
        index_a = m - 1
        index_b = n - 1
        while index_merged_array >= 0:
            if index_a < 0:
                A[index_merged_array] = B[index_b]
                index_b -= 1
            elif index_b < 0:
                A[index_merged_array] = A[index_a]
                index_a -= 1
            elif A[index_a] <= B[index_b]:
                A[index_merged_array] = B[index_b]
                index_b -= 1
            else:
                A[index_merged_array] = A[index_a]
                index_a -= 1
            index_merged_array -= 1

if __name__ == '__main__':
    solution = Solution()
    array_a = [1,3,5,7,9,0,0,0,0,0]
    array_b = [0,2,4,6,8]
    solution.merge(array_a, 5, array_b, 5)
    print array_a
