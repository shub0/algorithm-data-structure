#! /usr/bin/python

'''
 Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        size = len(A)
        for index in range(size):
            _index = index
            while True:
                num = A[_index]
                expected_index = num - 1
                if expected_index == _index or expected_index < 0 or expected_index >= size or num == A[expected_index]:
                    break
                tmp = num
                A[_index] = A[expected_index]
                A[expected_index] = num

        for index in range(size):
            if A[index] != index + 1:
                return index + 1
        return size + 1

if __name__ == '__main__':
    solution = Solution()
    print solution.firstMissingPositive([2,1,4,3])
