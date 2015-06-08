#! /usr/bin/python

'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

          1
        /   \
       2     5
      / \   / \
     3   4 10  6
    /
   7


'''

from node_struct import TreeNode

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodesSlow(self, root):
        nodes_in_tree = list()
        count = 0
        curr_node = root
        while len(nodes_in_tree) > 0 or curr_node:
            while curr_node:
                nodes_in_tree.append(curr_node)
                curr_node = curr_node.left
            curr_node = nodes_in_tree.pop()
            count += 1         # visit()
            curr_node = curr_node.right
        return count

    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        left_depth = 0
        curr_node = root
        while curr_node:
            left_depth += 1
            curr_node = curr_node.left
        curr_node = root
        right_depth = 0
        while curr_node:
            right_depth += 1
            curr_node = curr_node.right
        # full filled tree
        if left_depth == right_depth:
            return 2 ** left_depth - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(7)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(6)
    print solution.countNodes(root)
