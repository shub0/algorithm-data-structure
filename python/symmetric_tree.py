#! /usr/bin/python

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
'''

from node_struct import TreeNode
class Solution:
    def isSymmetricRecursive(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2
        elif node1.val !=  node2.val:
            return False
        else:
            return self.isSymmetricRecursive(node1.left, node2.right) \
                and self.isSymmetricRecursive(node1.right, node2.left)

    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmetricRecursive(root.left, root.right)

class SolutionNonRecursive:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        nodes_in_tree = list()
        nodes_in_tree.append((root.left, root.right))
        while len(nodes_in_tree) > 0:
            node1, node2 = nodes_in_tree.pop(0)
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                nodes_in_tree.append((node1.left, node2.right))
                nodes_in_tree.append((node1.right, node2.left))
        return True

if __name__ == '__main__':
    solution = Solution()
    solution_non_recursive = SolutionNonRecursive()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(2)
    print solution.isSymmetric(root)
    print solution_non_recursive.isSymmetric(root)
