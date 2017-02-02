#! /usr/bin/python

'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution:

    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if int(num1) == 0 or int(num2) == 0:
            return '0'
        if num1[0] == '-' and num2[0] == '-':
            return self.multiply(num1[1:], num2[1:])
        elif num1[0] == '-':
            return '-' + self.multiply(num1[1:], num2)
        elif num2[0] == '-':
            return '-' + self.multiply(num1, num2[1:])
        elif len(num2) > len(num1):
            return self.multiply(num2, num1)
        out = list()
        index = 0
        for char in num2[::-1]:
            current_product = self.multiply_simple(num1, char)
            out.append(current_product + ''.join( ['0'] * index))
            index += 1
        return self.add(out).lstrip('0')

    def add(self, array):
        OFFSET = 48
        carry = 0
        max_len = max([len(num) for num in array])
        out = list()
        _array = [ num.rjust(max_len, '0') for num in array ]
        print _array
        for index_len in range(max_len - 1, -1, -1):
            for num in _array:
                carry += (ord(num[index_len]) - OFFSET)
            digit = carry % 10
            carry = carry / 10
            out.append(chr(digit+OFFSET))
        if carry > 0:
            out.append(chr(carry+OFFSET))
        return ''.join(out[::-1])

    def multiply_simple(self, num1, digit):
        OFFSET = 48
        size = len(num1)
        carry = 0
        out = list()
        _digit = ord(digit) - OFFSET
        for char in num1[::-1]:
            current_product = (ord(char) - OFFSET) * _digit + carry
            current_digit   = current_product % 10
            carry = current_product / 10
            out.append(chr(current_digit + OFFSET))
        if carry > 0:
            out.append(chr(carry + OFFSET))
        return ''.join(out[::-1])

    def multiply2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        M = len(num1)
        N = len(num2)
        output = [0] * (M+N)
        for (m, digit1) in enumerate(num1[::-1]):
            for (n, digit2) in enumerate(num2[::-1]):
                product = output[m+n] + int(digit1) * int(digit2)
                output[m+n] = product % 10
                output[m+n+1] += product / 10
        return "".join([ str(digit) for digit in output[::-1] ]).lstrip("0")

if __name__ == '__main__':
    solution = Solution()
    print "expected: %d" % (140 * 721)
    print solution.multiply2('140','721')
