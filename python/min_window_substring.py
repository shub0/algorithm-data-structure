#! /usr/bin/python

'''
 Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution:
    # @return a string
    def minWindow(self, s, t):
        import collections
        dict_t = collections.defaultdict(int)
        dict_w = collections.defaultdict(int)
        size = len(s)
        for char in t:
            dict_t[char] += 1
        flag = False
        end = 0
        start = 0
        match = 0
        window = s
        total_char = len(dict_t.keys())
        while end < size:
            char = s[end]
            dict_w[char] += 1
            end += 1
            if dict_w[char] == dict_t[char]:
                match += 1

            if ( match == total_char ):
                flag = True
                while start < end:
                    _char = s[start]
                    dict_w[_char] -= 1
                    start += 1
                    if dict_w[_char] < dict_t[_char]:
                        match -= 1
                        break
                if (end-start+1) < len(window):
                    window = s[start-1:end]

        if flag:
            return window
        return ""

if __name__ == '__main__':
    solution = Solution()
    print solution.minWindow("ADOBECODEBANC", 'ABC')
