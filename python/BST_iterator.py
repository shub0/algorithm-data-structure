#! /usr/bin/python

'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''

from node_struct import TreeNode
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.path = list()
        next_node = root

        while next_node:
            self.path.append(next_node)
            next_node = next_node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.path) > 0


    # @return an integer, the next smallest number
    def next(self):
        res = self.path.pop()
        if res.right:
            next_node = res.right
            while next_node:
                self.path.append(next_node)
                next_node = next_node.left
        return res.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
