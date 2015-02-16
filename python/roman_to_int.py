#! /usr/bin/python

'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    def romanToInt(self, seq):
        MAX_VALUE = 4999
        romanChar = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
        previous = MAX_VALUE
        number = 0
        for element in seq:
            number += romanChar[element]
            if (romanChar[element] > previous):
                number -= 2 * previous
            previous = romanChar[element]
        return number

if __name__ == '__main__':
    solution = Solution()
    print solution.romanToInt('XII')

