'''
A password is considered strong if below conditions are all met:

1. It has at least 6 characters and at most 20 characters.
2. It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
3. It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
'''

class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        missing_type = 3
        if any('a' <= c <= 'z' for c in s):
            missing_type -= 1
        if any('A' <= c <= 'Z' for c in s):
            missing_type -= 1
        if any(c.isdigit() for c in s):
            missing_type -= 1
        delete_one = 0    # one deletion
        delete_two = 0    # two deletion
        replacement = 0
        index = 2
        while index < size:
            if s[index] == s[index-1] == s[index-2]:
                count = 2
                while ( (index < size) and (s[index] == s[index-1]) ):
                    count += 1
                    index += 1
                replacement += count / 3
                if (count%3 == 0):
                    delete_one += 1
                elif (count%3 == 1):
                    delete_two += 1
            else:
                index += 1
        if size < 6:
            return max(missing_type, 6 - size)
        elif size <= 20:
            return max(missing_type, replacement)
        else:
            delete = size - 20
            replacement -= min(delete, delete_one)
            replacement -= min(max(delete - delete_one, 0), delete_two*2) / 2
            replacement -= max(delete - delete_one - 2 * delete_two, 0) / 3
            return delete + max(missing_type, replacement)

solution = Solution()
print solution.strongPasswordChecker("abcdef")
print solution.strongPasswordChecker("aaa123")
print solution.strongPasswordChecker("aaa111")
print solution.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa")
print solution.strongPasswordChecker("ABABABABABABABABABAB1")
print solution.strongPasswordChecker("..................!!!")

