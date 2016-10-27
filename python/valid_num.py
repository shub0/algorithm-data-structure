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
    def isNumber(self, s, signed=False, sci = False, dot=False):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        size = len(s)
        if size < 1:
            return True
        if s[0] in "+-":
            return (not signed) and (self.isNumber(s[1:], True, sci, dot))
        for index in range(size):
            char = s[index]
            if char not in "0123456789e.":
                return False
            if char == "e":
                return (not sci) and (index > 0) and (index < size-1)  and (self.isNumber(s[index+1:], False, True, True))
            if char == ".":
                if dot: return False
                dot = True
        return True

if __name__ =='__main__':
    solution = Solution()
    a = ['0', '0.1', 'abc', '1 a', '2e10', "1e1.58", "e"]
    print [ solution.isNumber(string) for string in a ]
