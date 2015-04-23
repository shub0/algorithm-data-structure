#! /usr/bin/python


'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

if __name__ =='__main__':
    solution = Solution()
    a = ['0', '0.1', 'abc', '1 a', '2e10']
    print [ solution.isNumber(string) for string in a ]
