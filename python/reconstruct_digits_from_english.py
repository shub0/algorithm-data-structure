'''
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"
Output: "012"

Example 2:
Input: "fviefuro"
Output: "45"
'''


class Solution(object):
    def remove(self, chars, sig):
        count = self.freq[sig]
        for char in chars:
            self.freq[char] -= count
        return count

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        self.freq = collections.defaultdict(int)
        for char in s:
            self.freq[char] += 1
        output = list()
        output.append( ('0', self.remove("zero", "z")) )
        output.append( ('2', self.remove("two", "w")) )
        output.append( ('4', self.remove("four", "u")) )
        output.append( ('6', self.remove("six", "x")) )
        output.append( ('8', self.remove("eight", "g")) )
        output.append( ('1', self.remove("one", "o")) )
        output.append( ('3', self.remove("three", "h")) )
        output.append( ('5', self.remove("five", "f")) )
        output.append( ('7', self.remove("seven", "v")) )
        output.append( ('9', self.remove("nine", "i")) )
        output.sort(key = lambda x: x[0])
        res = list()
        for (digit, freq) in output:
            res += [digit] * freq
        return ''.join(res)

solution = Solution()
print solution.originalDigits("owoztneoer")
print solution.originalDigits("fviefuro")
