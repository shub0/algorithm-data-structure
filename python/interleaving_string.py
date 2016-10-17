#! /usr/bin/python

'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
For example,
Given:
s1 = "aabcc",
s2 = "dbbca",
When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        size1 = len(s1)
        size2 = len(s2)
        size3 = len(s3)
        if size1 < size2:
            return self.isInterleave(s2, s1, s3)
        if size1 + size2 != size3:
            return False
        if size1 == 0 and s2 != s3:
            return False
        if size1 == 0 and s2 == s3:
            return True
        dp_array = [ [True] * (size1 + 1) for _ in range(size2 + 1) ]
        for index1 in range(0, size1 + 1):
            for index2 in range(0, size2 + 1):
                if index1 == 0 and index2 == 0:
                    dp_array[index2][index1] = True
                elif index1 == 0:
                    dp_array[index2][index1] = (s2[:index2] == s3[:index2])
                elif index2 == 0:
                    dp_array[index2][index1] = (s1[:index1] == s3[:index1])
                else:
                    dp_array[index2][index1] =  (s1[index1 - 1] == s3[index1 + index2 -1] and dp_array[index2][index1-1]) or (s2[index2 - 1] == s3[index1 + index2 - 1] and dp_array[index2-1][index1])
        return dp_array[-1][-1]
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        size1 = len(s1)
        size2 = len(s2)
        size3 = len(s3)
        if (size1 > size2):
            return self.isInterleave(s2,s1,s3)
        if size1 == 0:
            return s2 == s3
        if size1 + size2 != size3:
            return False
        dp_array = [ [True] * (size2+1) for _ in range(size1+1) ]
        for index1 in range(1, size1+1):
            dp_array[index1][0] = (s1[:index1] == s3[:index1])
        for index2 in range(1, size2+1):
            dp_array[0][index2] = (s2[:index2] == s3[:index2])
        for index1 in range(1,size1+1):
            for index2 in range(1,size2+1):
                dp_array[index1][index2] = ( (s1[index1-1] == s3[index1+index2-1] and dp_array[index1-1][index2] ) or
                                         (s2[index2-1] == s3[index1+index2-1] and dp_array[index1][index2-1]) )
        return dp_array[size1][size2]

solution = Solution()
print solution.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
print solution.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
