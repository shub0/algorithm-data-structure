#! /usr/bin/python

'''
Binary Tree Traversal
'''

from node_struct import TreeNode

class Solution:
    def inOrderTraversal(self, root):
        output = list()
        self._inOrderTraversal(root, output)
        return output

    def _inOrderTraversal(self, root, output):
        if not root:
            return
        self.inOrderTraversal(root.left, output)
        output.append(root.val)
        self.inOrderTraversal(root.right, output)
        
    def preOrderTraversalNonRecursive(self, root):
        output = list()
        nodes_in_tree = list()
        current_node = root
        while len(nodes_in_tree) > 0 or current_node:
            while current_node:
                nodes_in_tree.append(current_node)
                output.append(current_node.val)
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
            output.append(current_node.val)
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

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    print 'pre order: %s'  % solution.preOrderTraversalNonRecursive(root)
    print 'in order: %s'   % solution.inOrderTraversalNonRecursive(root)
    print 'post order: %s' % solution.postOrderTraversalNonRecursive(root)

        
