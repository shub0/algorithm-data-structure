#! /usr/bin/python

'''
Given a list of non negative integers, arrange them such that they form the largest number.
For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:

    def largestNumber(self, num):
        if len(num) == 0:
            return '0';
        def my_comparator( str_a, str_b):
            _str_a = ''.join([str_a, str_b])
            _str_b = ''.join([str_b, str_a])
            if (_str_a > _str_b):
                return 1
            return -1
            
        str_list = [str(x) for x in num]

        result = ''.join(sorted(str_list, cmp=my_comparator, reverse=True)).lstrip("0")
        if len(result) > 0:
            return result
        return '0'

if __name__ == '__main__':
    solution = Solution()
    print solution.largestNumber([0,0])
