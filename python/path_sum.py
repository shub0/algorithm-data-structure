#! /usr/bin/python

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Follow up question:
Find all paths
'''


from node_struct import TreeNode

class Solution:
    def leafNode(self, root):
        if not root.left and not root.right:
            return True
        return False

    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if sum == root.val and self.leafNode(root):
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def findPath(self, root, sum, a_path, path_list):
        if not root:
            return
        if sum == root.val and self.leafNode(root):
            a_path.append(root.val)
            path_list.append(a_path[:])
        else:
            a_path.append(root.val)
            size = len(a_path)
            self.findPath(root.left, sum - root.val, a_path, path_list)
            a_path[:] = a_path[:size]
            self.findPath(root.right, sum - root.val, a_path, path_list)

    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        path_list = list()
        self.findPath(root, sum, list(), path_list)
        return path_list
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
    print solution.hasPathSum(root, 22)
    print solution.pathSum(root, 22)
