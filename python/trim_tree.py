#! /usr/bin/python

'''
Give a tree with live/dead nodes
live nodes are defined as val > 0, dead nodes are defined as val = 0
Modify the tree so that if the root node is dead then the whole tree nodes must be dead
         1
        / \
       2   0
      / \   \
     3   4   6
          \
           7

Trimed as
         1
        / \
       2   0
      / \   \
     3   4   0
          \
           7

'''

from node_struct import TreeNode
class Solution:
    def trimTree(self, root, status=1):
        if not root:
            return
        if status == 0:
            root.val = 0
        self.trimTree(root.left, root.val)
        self.trimTree(root.right, root.val)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.right = TreeNode(7)
    root.left.right = TreeNode(4)
    root.right = TreeNode(0)
    root.right.right = TreeNode(6)
    solution.trimTree(root)
    print root.right.right.val
    print root.left.left.val
