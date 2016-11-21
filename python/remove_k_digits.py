'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be >= k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        val = str(num)
        output = list()
        for char in val:
            while len(output) > 0 and output[-1] > char and k > 0:
                output.pop()
                k -= 1
            output.append(char)
        out = "".join(output).lstrip("0")
        size = len(out)
        print size
        print k
        if size > k:
            return out[:size-k]
        return "0"

solution = Solution()
print solution.removeKdigits("10200", 2)
print solution.removeKdigits("10", 2)
print solution.removeKdigits("1432219", 3)
print solution.removeKdigits("12345", 2)
print solution.removeKdigits("9", 1)
print solution.removeKdigits("126345", 2)
print solution.removeKdigits("10", 1)
