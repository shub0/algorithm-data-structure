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
    def minWindow(self, S, T):
        import collections
        dict_T = collections.defaultdict(int)
        dict_S = collections.defaultdict(int)
        size_T = len(set(T))
        size_S = len(S)
        for char in T:
            dict_T[char] += 1
        start = 0
        end   = 0
        match = 0
        flag  = False
        min_window = S
        while end < size_S:
            char = S[end]
            dict_S[char] += 1
            if dict_S[char] == dict_T.get(char, 0):
                match += 1
            if match == size_T:
                flag = True
                while start <= end:
                    char = S[start]
                    dict_S[char] -= 1
                    start += 1
                    if dict_S[char] < dict_T[char]:
                        match -= 1
                        break
                if end - start + 2 < len(min_window):
                    min_window = S[start-1: end+1]
            end += 1
        if flag:
            return min_window
        return ''

if __name__ == '__main__':
    solution = Solution()
    print solution.minWindow("ADOBECODEBANC", 'ABC')
