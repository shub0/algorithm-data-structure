#! /usr/bin/python

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:
    # @param char, a character
    # @return a boolean
    def isLowerAlphanumeric(self,char):
        return (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('0') and ord(char) <= ord('9'))

    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        size = len(s)
        if size < 2:
            return True
        _s = s.lower()
        left_index = 0
        right_index = size - 1
        while (left_index < right_index):
            if not self.isLowerAlphanumeric(_s[left_index]):
                left_index += 1
                continue
            if not self.isLowerAlphanumeric(_s[right_index]):
                right_index -= 1
                continue
            if _s[left_index] != _s[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    print solution.isPalindrome("A man, a plan, a canal: Panama")
