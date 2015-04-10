#! /usr/bin/python

'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeNonRecursive(self, p, q):
        nodes_in_tree = list()
        nodes_in_tree.append((p, q))
        while len(nodes_in_tree) > 0:
            node1, node2 = nodes_in_tree.pop(0)
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                nodes_in_tree.append((node1.left, node2.left))
                nodes_in_tree.append((node1.right, node2.right))
        return True
