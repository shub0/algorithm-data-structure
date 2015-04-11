#! /usr/bin/python
'''
Given a binary tree, flatten it to a linked list in-place.
For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''

from node_struct import TreeNode
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root:
            right_node = root.right
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            self.flatten(right_node)
            cursor = root
            while cursor.right:
                cursor = cursor.right
            cursor.right = right_node

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    solution.flatten(root)
    while root:
        print root.val
        root = root.right
