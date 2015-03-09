#! /usr/bin/python

'''
Problem 1:

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Problme 2:
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        cursor = 0
        for index in range(len(A)):
            if A[index] == A[cursor]:
                continue
            cursor += 1
            A[cursor] = A[index]
        return cursor + 1

    # @param A a list of integers
    # @return an integer
    def removeDuplicates2(self, A):
        if len(A) < 3:
            return len(A)
        cursor = 1
        for index in range(2,len(A)):
            if (A[index] == A[cursor] and A[cursor] != A[cursor-1]) or (A[index] != A[cursor]):
                cursor += 1
                A[cursor] = A[index]
        return cursor + 1

if __name__ == '__main__':
    solution = Solution()
    A = [1,2,3,4]
    B = [1,1,1,2,2,3]
    solution.removeDuplicates2(B)
    solution.removeDuplicates2(A)
    print A
    print B
                
