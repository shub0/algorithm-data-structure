#! /usr/bin/python

'''
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    def intToRoman(self, num):
        TENS = ['I', 'X', 'C', 'M']
        FIVES = ['V', 'L', 'D']
        offset = 0
        roman = list()
        while (num > 0):
            digit = num % 10
            num /= 10
            flag = False
            if (digit == 9):
                roman.append(TENS[offset+1])
                roman.append(TENS[offset])
                digit = 0
            elif (digit == 4):
                roman.append(FIVES[offset])
                roman.append(TENS[offset])
                digit = 0
            elif (digit >= 5):
                flag = True
                digit -= 5
            roman.append(TENS[offset] * digit)
            if (flag): roman.append(FIVES[offset])
            offset +=1
        return ''.join(roman[::-1])

if __name__ == '__main__':
    solution = Solution()
    print solution.intToRoman(19)
