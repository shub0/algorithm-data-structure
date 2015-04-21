#! /usr/bin/python


'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''

from node_struct import TreeNode

class Solution:
    def get_first(self, root, counts, node):
        if not root:
            return node
        node = self.get_first(root.left, counts, node)
        if root.val < counts[0]:
            node = root
        counts[0] = root.val
        node = self.get_first(root.right, counts, node)
        return node

    def get_second(self, root, counts, node):
        if not root:
            return node
        node = self.get_second(root.right, counts, node)
        if root.val > counts[1]:
            node = root
        counts[1] = root.val
        node = self.get_second(root.left, counts, node)
        return node

    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        node1 = None
        node2 = None
        counts = [1e10, -1e10]
        node1 = self.get_first(root, counts, node1)
        node2 = self.get_second(root, counts, node2)
        node1.val, node2.val = node2.val, node1.val

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution.recoverTree(root)
    print root.left.val
