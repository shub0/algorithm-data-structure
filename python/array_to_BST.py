#! /usr/bin/python

'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

from node_struct import TreeNode
class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        size = len(num)
        if size == 0:
            return None
        if size == 1:
            return TreeNode(num[0])
        root = TreeNode(num[size / 2])
        root.left = self.sortedArrayToBST(num[ :size/2])
        root.right = self.sortedArrayToBST(num[size/2+1: ])
        return root

if __name__ == '__main__':
    solution = Solution()
    root = solution.sortedArrayToBST(range(1,8))
    print root.val, root.left.val, root.right.val
