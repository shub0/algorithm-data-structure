#! /usr/bin/python

'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Given preorder and inorder traversal of a tree, construct the binary tree.
'''

from node_struct import TreeNode
class Solution:
    def _buildTreeInPostOrder(self, inorder, start_index_inorder, end_index_inorder, postorder, start_index_postorder, end_index_postorder):
        size = end_index_inorder - start_index_inorder + 1
        if size == 0:
            return None
        if size == 1:
            return TreeNode(inorder[start_index_inorder])
        root_val = postorder[end_index_postorder]
        root_node = TreeNode(root_val)
        root_index = inorder.index(root_val)
        left_tree_size = root_index - start_index_inorder
        right_tree_size = end_index_inorder - root_index

        root_node.left = self._buildTreeInPostOrder(inorder, start_index_inorder, root_index-1, postorder, start_index_postorder, root_index-start_index_inorder+start_index_postorder-1)
        root_node.right = self._buildTreeInPostOrder(inorder, root_index + 1, end_index_inorder, postorder, end_index_postorder-end_index_inorder+root_index, end_index_postorder-1)
        return root_node

    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTreeInPostOrder(self, inorder, postorder):
        size = len(inorder)
        if size == 0:
            return None
        if size == 1:
            return TreeNode(inorder[0])
        return self._buildTreeInPostOrder(inorder, 0, size-1, postorder, 0, size-1)

    def _buildTreePreInOrder(self, preorder, inorder, start_index_preorder, start_index_inorder, size):
        if size == 0:
            return None
        if size == 1:
            return TreeNode(inorder[start_index_inorder])
        else:
            root_val = preorder[start_index_preorder]
            root_node = TreeNode(root_val)
            root_index = inorder.index(root_val)
            left_tree_size = root_index - start_index_inorder
            right_tree_size = size - 1 - left_tree_size
            root_node.left = self._buildTreePreInOrder(preorder, inorder, start_index_preorder+1,start_index_inorder, left_tree_size)
            root_node.right = self._buildTreePreInOrder(preorder, inorder, start_index_preorder+1+left_tree_size, root_index+1, right_tree_size)
            return root_node

    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTreePreInOrder(self, preorder, inorder):
        size = len(inorder)
        if size == 0:
            return None
        elif size == 1:
            return TreeNode(preorder[0])
        else:
            return self._buildTreePreInOrder(preorder, inorder, 0, 0, size)

if __name__ == '__main__':
    inorder   = [2,4,6,8,9,10,11,12,14]
    postorder = [2,6,4,9,11,10,14,12,8]
    preorder  = [8,4,2,6,12,10,9,11,14]
    solution = Solution()
    root = solution.buildTreeInPostOrder(inorder, postorder)
    print root.val, root.left.val, root.right.val
    root = solution.buildTreePreInOrder(preorder, inorder)
    print root.val, root.left.val, root.right.val
