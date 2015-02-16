#! /usr/bin/python

'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 13.37
'''

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v_1 = [ int(digit) for digit in version1.strip().split('.') ]
        v_2 = [ int(digit) for digit in version2.strip().split('.') ]
        if (len(v_1) < len(v_2)): return -1 * self.compareVersion(version2, version1)
        for index in range(len(v_2)):
            if (v_1[index] > v_2[index]): return 1
            elif (v_1[index] < v_2[index]): return -1
        if (len(v_1) == len(v_2) or sum(v_1[len(v_2):]) == 0): 
            return 0
        return 1

if __name__ == '__main__':
    solution = Solution()
    print solution.compareVersion('1.0.1', '1')
