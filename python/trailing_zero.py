#! /bin/usr/python

class Solution():
    def trailingZeros(self, n):
        trailingZeros = 0
        base = 5
        while (base <= n):
             trailingZeros += n / base
             base *= 5
        return trailingZeros

if __name__ == '__main__':
    solution = Solution()
    print solution.trailingZeros(19)
