#! /usr/bin/python

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if (numerator * denominator < 0):
            return '-%s' % (self.fractionToDecimal(-1 * numerator, denominator))
        residual = {}
        _result = []
        _result.append(str(numerator/denominator))
        _result.append('.')
        _residual = numerator % denominator
        index = 0
        residual[_residual] = index
        start = 0
        end = 0
        if (_residual == 0):
           return str(numerator/denominator)
        while(_residual != 0):
            index += 1
            _result.append(str(_residual * 10 / denominator))
            _residual = _residual * 10 % denominator
            if _residual in residual.keys():
	        start = residual[_residual]
                end = index
                break
            residual[_residual] = index
	decimal = 2
        if (_residual == 0):
            result = str((1.0 * numerator / denominator))
        else:
            result = '%s(%s)' % (''.join(_result[:decimal + start]),''.join( _result[decimal+start:decimal+end]))
        return result.rstrip('.0')
if __name__ == '__main__':
	solution = Solution()
	print solution.fractionToDecimal(12, -7)
