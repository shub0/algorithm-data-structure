#! /usr/bin/python


'''
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        output = [''] * numRows
        index = 0
        direction = 1
        for char in s:
            output[index] += char
            index += direction
            if index == numRows or index == -1:
                direction *= -1
                index += 2 * direction
        return ''.join(output)

if __name__ == '__main__':
    solution = Solution()
    print solution.convert("PAYPALISHIRING", 2)
