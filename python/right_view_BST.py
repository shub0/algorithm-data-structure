#! /usr/bin/python

'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
         1          <-----
        / \
       2   5        <-----
      / \   \
     3   4   6      <-----
          \
           7        <------
You should return [1, 5, 6, 7].
'''

from node_struct import TreeNode


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        output = list()
        nodes_in_tree = list()
        if not root:
            return output
        nodes_in_tree.append(root)
        nodes_in_tree.append(None)
        value = root.val
        while len(nodes_in_tree) > 0:
            node = nodes_in_tree.pop(0)
            if not node:
                output.append(value)
                if len(nodes_in_tree) > 0:
                    nodes_in_tree.append(None)
            else:
                value = node.val
                if node.left:
                    nodes_in_tree.append(node.left)
                if node.right:
                    nodes_in_tree.append(node.right)
        return output

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.right = TreeNode(7)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print solution.rightSideView(root)
