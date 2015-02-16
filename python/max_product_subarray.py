#! /usr/bin/python

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def maxProduct(self, num):
        size = len(num)
        if size == 0:
            return 0
        if size == 1:
            return num[0]
        max_product = num[0]
        min_product = num[0]
        curr_max_product = max_product
        for element in num[1:]:
            if element > 0:
                max_product = max(element, element * max_product)
                min_product = min(element, element * min_product)
            else:
                temp_max_product = max_product
                max_product = max(element, element * min_product)
                min_product = min(element, element * temp_max_product)
            curr_max_product = max(curr_max_product, max_product)
        return curr_max_product

if __name__ == '__main__':
    solution = Solution()
    print solution.maxProduct([2,3,-2,4])
