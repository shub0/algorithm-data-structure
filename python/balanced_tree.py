#! /usr/bin/python

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

              5
             / \
            4   8
           / \ / \
          11 1 3  4
         /  \    / \
        7    2  5   1
'''

from node_struct import TreeNode
class Solution:
    def getDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        else:
            diff = self.getDepth(root.left) - self.getDepth(root.right)
            if diff > 1 or diff < -1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.right = TreeNode(1)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print solution.isBalanced(root)
