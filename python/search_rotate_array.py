#! /usr/bin/python

'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, num, target):
        start = 0
        end   = len(num) - 1
        while start <= end:
            middle = (end - start) / 2 + start
            if num[middle] == target:
                return middle
            # First half not rotated, first half rotated
            elif num[start] < num[middle]:
                # In the first half
                if num[start] <= target and target <= num[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            # First half rotated, second half not rotated
            elif num[start] > num[middle]:
                # In the second half
                if num[middle] < target and target <= num[end]:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                start += 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    print solution.search([5,6,6,7,1,2,3,4], 6)


