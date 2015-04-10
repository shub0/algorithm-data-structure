#! /usr/bin/python

'''
Binary Tree Traversal
'''

from node_struct import TreeNode

class Solution:
    def preOrderTraversalNonRecursive(self, root):
        output = list()
        nodes_in_tree = list()
        current_node = root
        while len(nodes_in_tree) > 0 or current_node:
            while current_node:
                output.append(current_node.val)    # visit()
                nodes_in_tree.append(current_node)
                current_node = current_node.left
            current_node = nodes_in_tree.pop()
            current_node = current_node.right
        return output

    def inOrderTraversalNonRecursive(self, root):
        output = list()
        nodes_in_tree = list()
        current_node = root
        while len(nodes_in_tree) > 0 or current_node:
            while current_node:
                nodes_in_tree.append(current_node)
                current_node = current_node.left
            current_node = nodes_in_tree.pop()
            output.append(current_node.val)    # visit()
            current_node = current_node.right
        return output

    def postOrderTraversalNonRecursive(self, root):
        output = list()
        nodes_in_tree = list()
        current_node = root
        prev_node = None
        while current_node:
            while current_node.left:
                nodes_in_tree.append(current_node)
                current_node = current_node.left
            while not current_node.right or current_node.right == prev_node:
                output.append(current_node.val)
                prev_node = current_node
                if len(nodes_in_tree) == 0:
                    return output
                current_node = nodes_in_tree.pop()
            nodes_in_tree.append(current_node)
            current_node = current_node.right
        return output

    def levelOrderTraversal(self, root):
        output = list()
        if not root:
            return output
        nodes_in_tree = list()
        nodes_in_tree.append(root)
        nodes_in_tree.append(None)
        curr_level = list()
        while len(nodes_in_tree) > 0:
            current_node = nodes_in_tree.pop(0)
            if not current_node:
                output.append(curr_level[:])
                curr_level = list()
                if len(nodes_in_tree) > 0:
                    nodes_in_tree.append(None)
                else:
                    return output
            else:
                curr_level.append(current_node.val)
                if current_node.left:
                    nodes_in_tree.append(current_node.left)
                if current_node.right:
                    nodes_in_tree.append(current_node.right)
        return output


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print 'pre order: %s'  % solution.preOrderTraversalNonRecursive(root)
    print 'in order: %s'   % solution.inOrderTraversalNonRecursive(root)
    print 'post order: %s' % solution.postOrderTraversalNonRecursive(root)
    print 'level order: %s'% solution.levelOrderTraversal(root)
