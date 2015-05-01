#! /usr/bin/python

'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.
'''

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        if n < 1 or n > 9 or k <= 0:
            raise ValueError('n mubst be between 1 and 9 inclusive and k must be positive')
        sequence_digit = range(1, n+1)
        max_k = [1] * n
        for index in range(1, n):
            max_k[index] = max_k[index-1] * (index+1)
        if k > max_k[n-1]:
            raise ValueError('k is too large for given n')
        output = list()
        index = n - 2
        k = k - 1
        while len(sequence_digit) > 0:
            current_digit = k / max_k[index]
            output.append('%d' % sequence_digit[current_digit])
            del sequence_digit[current_digit]
            k %= max_k[index]
            index -= 1
        return ''.join(output)

if __name__ == '__main__':
    solution = Solution()
    print solution.getPermutation(9,2)
