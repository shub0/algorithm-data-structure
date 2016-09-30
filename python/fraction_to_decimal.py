#! /usr/bin/python

'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

For example,
Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negative = ""
        if numerator * denominator < 0:
            negative = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        decimal = numerator / denominator
        output = list()
        res = numerator % denominator
        index = 0
        res_set = dict()
        while (res > 0):
            res_set[res] = index
            res = res * 10
            digit = res / denominator
            res = res % denominator
            output.append(str(digit))
            if res in res_set:
                break
            index += 1

        def formatDecimal():
            if len(output) == 0:
                return ""
            elif (res == 0):
                return "." + "".join(output)
            else:
                start = res_set[res]
                return "." + "".join(output[:start]) + "(" + "".join(output[start:]) + ")"
        return negative + str(decimal) + formatDecimal()

if __name__ == '__main__':
	solution = Solution()
	print solution.fractionToDecimal(1,13)
