#! /usr/bin/python

'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

from node_struct import TreeNode
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        else:
            if not root.left:
                return 1 + self.minDepth(root.right)
            if not root.right:
                return 1 + self.minDepth(root.left)
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(0)
    print solution.minDepth(root)
