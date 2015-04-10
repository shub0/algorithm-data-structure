#! /usr/bin/python

'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,
              5
             / \
            4  -8
           /   / \
         -11  13  4
         /  \    / \
        7    2  5   1
Return 14.
'''

from node_struct import TreeNode
class Solution:
    def maxPathSumRecursive(self, root, max_sum):
        if not root:
            return 0
        left_sum = self.maxPathSumRecursive(root.left, max_sum)
        right_sum = self.maxPathSumRecursive(root.right, max_sum)
        # visit logic
        local_max_sum = root.val
        if left_sum > 0:
            local_max_sum += left_sum
        if right_sum > 0:
            local_max_sum += right_sum
        max_sum[0] = max(max_sum[0], local_max_sum)
        return root.val + max(0, max(left_sum, right_sum))

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if not root:
            return 0
        max_sum = [-1e8]
        self.maxPathSumRecursive(root,max_sum)
        return max_sum[0]


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(-11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(-8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print solution.maxPathSum(root)
