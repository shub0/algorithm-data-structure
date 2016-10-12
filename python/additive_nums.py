'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
'''


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        size = len(num)
        if size == 0:
            return True
        def dfs(start, num1, num2):
            if (start == size):
                return True
            if num1[0] == '0' and len(num1) > 1: return False
            if num2[0] == '0' and len(num2) > 1: return False
            if num[start] == '0':
                if num1 == '0' and num2 == '0':
                    return dfs(start+1, num2, '0')
                else:
                    return False
            for index in range(start+1, size+1):
                if int(num[start:index]) == (int(num1) + int(num2)) and dfs(index, num2, num[start:index]):
                    return True
            return False
        for start in range(1, size):
            for end in range(start+1, size):
                if dfs(end, num[:start], num[start:end]):
                    return True
        return False

solution = Solution()
print solution.isAdditiveNumber("1203")
