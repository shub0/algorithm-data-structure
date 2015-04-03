#! /usr/bin/python
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        return strs[0][:self.longestPrefix(strs)]

    def longestPrefix(self, strs):
        max_len = max([ len(_str) for _str in strs ])
        size    = len(strs)
        index   = 0
        while index < max_len:
            if index >= len(strs[0]):
                return index
            char = strs[0][index]
            for _str in strs[1:]:
                if len(_str) <= index or _str[index] != char:
                    return index
            index += 1
        return max_len



if __name__ == '__main__':
    solution = Solution()
    print solution.longestCommonPrefix([])
