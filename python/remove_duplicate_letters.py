'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''

class Solution(object):
    def toIndex(self, char):
        return ord(char) - ord('a')

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 26
        for char in s:
            count[self.toIndex(char)] += 1
        stack = list()
        visited = [False] * 26
        for char in s:
            index = self.toIndex(char)
            count[index] -= 1
            if visited[index]:
                continue
            while stack and stack[-1] > char and count[self.toIndex(stack[-1])] > 0:
                visited[self.toIndex(stack.pop())] = False
            visited[index] = True
            stack.append(char)

        return "".join(stack)

solution = Solution()
print("Expected acdb, got")
print(solution.removeDuplicateLetters("cbacdcbc"))
