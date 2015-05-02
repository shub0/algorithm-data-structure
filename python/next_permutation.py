#! /usr/bin/python

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
'''

class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        size = len(num)
        if size < 2:
            return
        for pos1 in range(size-1, -1, -1):
            for pos2 in range(pos1, -1, -1):
                if num[pos1] > num[pos2]:
                    num[pos1], num[pos2] = num[pos2], num[pos1]
                    num[pos2+1:] = sorted(num[pos2+1:])
                    return
        num.sort()

if __name__ == '__main__':
    solution = Solution()
    num = [1,1,5]
    solution.nextPermutation(num)
    print num
    num = [1,3,2]
    num = [3,2,1]
    solution.nextPermutation(num)
    print num
