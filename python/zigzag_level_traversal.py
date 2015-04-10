#! /usr/bin/python

'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

from node_struct import TreeNode

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        output = list()
        if not root:
            return output
        nodes_in_tree = list()
        current_level = list()
        nodes_in_tree.append(root)
        nodes_in_tree.append(None)
        reverse_order = False
        while len(nodes_in_tree) > 0:
            current_node = nodes_in_tree.pop(0)
            if not current_node:
                if reverse_order:
                    output.append(current_level[::-1])
                    reverse_order = False
                else:
                    output.append(current_level[:])
                    reverse_order = True
                current_level = list()
                if len(nodes_in_tree) > 0:
                    nodes_in_tree.append(None)
            else:
                current_level.append(current_node.val)
                if current_node.left:
                    nodes_in_tree.append(current_node.left)
                if current_node.right:
                    nodes_in_tree.append(current_node.right)
        return output

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print solution.zigzagLevelOrder(root)
