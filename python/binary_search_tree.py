#! /usr/bin/python


'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

from node_struct import TreeNode
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        if root.left:
            max_node = root.left
            while max_node.right:
                max_node = max_node.right
            if root.val <= max_node.val:
                return False
        if root.right:
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            if root.val >= min_node.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def inOrder(self, root, output):
        if not root:
            return
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)

    def isValidBST2(self, root):
        output = list()
        self.inOrder(root, output)
        for index in range(1,len(output)):
            if output[index] <= output[index-1]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right = TreeNode(12)
    print solution.isValidBST2(root)
