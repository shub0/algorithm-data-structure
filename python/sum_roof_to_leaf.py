#! /usr/bin/python

'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.
'''

from node_struct import TreeNode
class Solution:
    def leafNode(self, root):
        if not root.left and not root.right:
            return True
        return False

    def inOrderTraversal(self, root, currentPath, path):
        if not root:
            return
        # visit()
        currentPath = 10 * currentPath + root.val
        if self.leafNode(root):
            path.append(currentPath)
        else:
            self.inOrderTraversal(root.left, currentPath, path)
            self.inOrderTraversal(root.right, currentPath, path)

    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        path = list()
        self.inOrderTraversal(root, 0, path)
        return sum(path)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(5)
    print solution.sumNumbers(root)
    print solution.sumNumbers(None)
