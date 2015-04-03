#! /usr/bin/python

'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        segments    = path.split('/')
        simple_path = list()
        for segment in segments:
            if segment == '.':
                continue
            elif segment == '..':
                if len(simple_path) > 0 :
                    del simple_path[-1]
            elif len(segment) > 0:
                simple_path.append(segment)
        return '/' + '/'.join(simple_path)

if __name__ == '__main__':
    solution = Solution()
    print solution.simplifyPath('/home/')
    print solution.simplifyPath('/a/./b/../../c/')
