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
        if (denominator == 0):
            return 0
        if numerator % denominator == 0:
            return str(numerator / denominator)
        if (numerator > 0 and denominator < 0): return '-%s' % self.fractionToDecimal(numerator, -denominator)
        if (numerator < 0 and denominator > 0): return '-%s' % self.fractionToDecimal(-numerator, denominator)
        if (numerator < 0 and denominator < 0): return self.fractionToDecimal(-numerator, -denominator)
        
        result = [ str(numerator / denominator), '.' ]
        residual = numerator % denominator
        residual_dict = dict()
        residual_dict[residual] = len(result)
        while (residual > 0):
            result.append(str(10 * residual / denominator))
            residual = (10 * residual) % denominator
            if (residual in residual_dict.keys()):
                result.append(')')
                break
            residual_dict[residual] = len(result)
        if (residual == 0):
            return ''.join(result)
        first_index = residual_dict[residual]
        result.insert(first_index, '(')
        return ''.join(result)

if __name__ == '__main__':
	solution = Solution()
	print solution.fractionToDecimal(1,13)
