#! /usr/bin/python

'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return
        tmp_right = self.invertTree(root.left)
        tmp_left  = self.invertTree(root.right)
        root.left = tmp_left
        root.right = tmp_right
        return root
