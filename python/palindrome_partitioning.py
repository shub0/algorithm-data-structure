#! /usr/bin/python

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
Additional quesiton:
Return the minimal cut for partition
'''


class Solution:
        # @param s, a string
    # @return boolean
    def palindrome(self, s):
        return s == s[::-1]

    # @param s, a string
    # @return a list of string
    def partition_recursive(self, output_list, a_list, s):
        if not s:
            output_list.append(a_list[:])
        for index in range(1, len(s) + 1):
            start_string = s[:index]
            if self.palindrome(start_string):
                a_list.append(start_string)
                self.partition_recursive(output_list, a_list, s[index:])
                a_list.pop()

    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s:
            return []
        output_list = list()
        self.partition_recursive(output_list, list(), s)
        return output_list

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        size = len(s)
        if size == 0:
            return 0
        # build palindrome determination array
        is_pal = [ [False] * size for index in range(size) ]
        for index1 in range(size):
            for index2 in range(index1+1):
                if s[index2] == s[index1] and (index1-index2 < 2 or is_pal[index2+1][index1-1]):
                    is_pal[index2][index1] = True

        cut = range(size)
        for index1 in range(size):
            for index2 in range(index1+1):
                if is_pal[index2][index1]:
                    if index2 == 0:
                        cut[index1] = 0
                    else:
                        cut[index1] = min(cut[index1], cut[index2-1] + 1)
        return cut[-1]

if __name__ == '__main__':
    solution = Solution()
    print solution.minCut('aaabaa')
