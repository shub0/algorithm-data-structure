'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''


class Solution(object):
    def dfs(self, s):
        substring = list()
        digit = 0
        while self.index < len(s):
            char = s[self.index]
            self.index += 1
            if char in '0123456789':
                digit = digit * 10 + int(char)
            elif char == "[":
                substring += digit * self.dfs(s)
                digit = 0
            elif char == "]":
                return substring
            else:
                substring.append(char)
        return substring

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.index = 0
        return "".join(self.dfs(s))

solution = Solution()
print "Expected aaabcbc, got %s" % solution.decodeString("3[a]2[bc]")
print "Expected accaccacc, got %s" % solution.decodeString("3[a2[c]]")
print "Expected abcabccdcdcdef, got %s" % solution.decodeString("2[abc]3[cd]ef")
