'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet. 
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = list()
        N = 26
        OFFSET = 64
        while (num > 0):
            if (num % N == 0):
                result.append('Z')
                num -= N
            else:
                result.append(chr(num % N + OFFSET))
            num /= N
        return ''.join(result[::-1])

if __name__ == '__main__':
    solution = Solution()
    print solution.convertToTitle(27)
