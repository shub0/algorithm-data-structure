#! /usr/bin/python

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

Follow up:
Get the previous permutation in the sequence

'''

class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        size = len(num)
        if size < 2:
            return num
        pos = size - 2
        while pos > -1 and num[pos] >= num[pos+1]:
            pos -= 1
        print pos
        if pos > -1:
            for index in range(size - 1, pos, -1):
                if num[index] > num[pos]:
                    break
            num[pos], num[index] = num[index], num[pos]
        self.reverse(num, pos + 1, size - 1)

    def previousPermutation(self, num):
        size = len(num)
        pos = size - 2
        while pos > -1 and num[pos] <= num[pos+1]:
            pos -= 1
        if pos > -1:
            for index in range(size - 1, pos, -1):
                if num[index] < num[pos]:
                    break
            num[pos], num[index] = num[index], num[pos]
        self.reverse(num, pos+1, size-1)

    def reverse(self, num, start, end):
        while start < end:
            num[start], num[end] = num[end], num[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    solution = Solution()
    num = [4,2,0,2,3,2,0]
    solution.nextPermutation(num)
    print num
    solution.previousPermutation(num)
    print num
