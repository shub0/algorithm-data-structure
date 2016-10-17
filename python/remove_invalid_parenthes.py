'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for char in s:
                if char == "(":
                    cnt += 1
                if char == ")":
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        all_string = {s}
        while True:
            valid_string = filter(isValid, all_string)
            if valid_string:
                return valid_string
            all_string = {s[:i] + s[i+1:] for i in range(len(s)) for s in all_string}


    def remove(self, string, last_i, last_j, chars):
        # string to check
        # last_i: last valid index
        # last_j: last removal index
        # chars: chars of interest
        cnt = 0
        size = len(string)
        for i in range(last_i, size):
            if string[i] == chars[0]:
                cnt += 1
            if string[i] == chars[1]:
                cnt -= 1
            if cnt >= 0:
                continue
            for j in range(last_j, i+1):
                if (string[j] == chars[1]) and (j == last_j or string[j-1] != chars[1]):
                    self.remove(string[:j] + string[j+1:], i, j, chars)
            return
        reversed = string[::-1]
        if (chars[0] == "("):
            self.remove(reversed, 0, 0, ")(")
        else:
            self.output.append(reversed)

    def removeInvalidParenthesesQuick(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.output = list()
        self.remove(s, 0, 0, "()")
        return self.output

solution = Solution()
print """Expected ["()()()", "(())()"]"""
print solution.removeInvalidParenthesesQuick("()())()")

print """Expected ["(a)()()", "(a())()"]"""
print solution.removeInvalidParenthesesQuick("(a)())()")
