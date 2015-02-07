class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = list()
        N = 26
        while (num > 26):
            if (num % N == 0):
                result.append('Z')
                num -= N
            else:
                result.append(chr(num % N + 64))
            num /= N
        result.append(chr(num + 64))
        return ''.join(result[::-1])
