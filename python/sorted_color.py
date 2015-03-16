#! /usr/bin/python

'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
Please do the sorting in a one-pass algorithm
'''

class Solution:
    # @param data A list of 
    def switch(self, data, index_src, index_dest):
        if index_src == index_dest:
            return
        tmp = data[index_dest]
        data[index_dest] = data[index_src]
        data[index_src] = tmp

    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        size = len(A)
        index0 = 0
        index1 = index0
        index2 = size - 1
        while (index1 <= index2 and index0 <= index2):
            #print '%d, %d, %d' % (index0, index1, index2)
            if A[index1] == 0:
                self.switch(A, index0, index1)
                while index0 <= index2 and A[index0] == 0:
                    index0 += 1
                index1 = index0
            elif A[index1] == 2:
                self.switch(A, index1, index2)
                while index2 >= index1 and A[index2] == 2:
                    index2 -= 1
            else:
                index1 += 1

if __name__ == '__main__':
    solution = Solution()

    A = [1,0,0,0,2]
    solution.sortColors(A)
    print A
    A = [1,0,2,0,0,1,1,2]
    solution.sortColors(A)
    print A

    A = [2,1,0]
    solution.sortColors(A)
    print A
