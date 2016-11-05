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

    def printReverse(self, start, end, output):
        self.reverse(start, end)
        curr = end
        while True:
            output.append(curr.val)
            if (curr == start):
                break
            curr = curr.right
        self.reverse(start, end)


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

    def preorderMorris(self, root):
        curr = root
        output = list()
        while curr:
            if not curr.left:
                output.append(curr.val)
                curr = curr.right
            else:
                cursor = curr.left
                while cursor.right and cursor.right != curr:
                    cursor = cursor.right
                if cursor.right == curr:
                    cursor.right = None
                    curr = curr.right
                else:
                    output.append(curr.val)
                    cursor.right = curr
                    curr = curr.left
        return output

    def inorderMorris(self, root):
        curr = root
        output = list()
        while curr:
            if not curr.left:
                output.append(curr.val)
                curr = curr.right
            else:
                cursor = curr.left
                while cursor.right and cursor.right != curr:
                    cursor = cursor.right
                if not cursor.right:
                    cursor.right = curr
                    curr = curr.left
                else:
                    cursor.right = None
                    output.append(curr.val)
                    curr = curr.right
        return output
    def reverse(self, start, end):
        if start == end:
            return
        x, y = start, start.right
        while x != end:
            z = y.right
            y.right = x
            x = y
            y = z

    def postorderMorris(self, root):
        pivot = TreeNode(0)
        pivot.left = root
        curr = pivot
        output = list()

        def printReverse(start, end):
            self.reverse(start, end)
            curr = end
            while True:
                output.append(curr.val)
                if (curr == start):
                    break
                curr = curr.right
            self.reverse(end, start)

        while curr:
            if not curr.left:
                curr = curr.right
                continue
            cursor = curr.left
            while cursor.right and cursor.right != curr:
                cursor = cursor.right
            if not cursor.right:
                cursor.right = curr
                curr = curr.left
            else:
                printReverse(curr.left, cursor)
                cursor.right = None
                curr = curr.right
        return output

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print 'pre order: %s'  % solution.preOrderTraversalNonRecursive(root)
    print 'pre order: %s'  % solution.preorderMorris(root)
    print 'in order: %s'   % solution.inOrderTraversalNonRecursive(root)
    print 'in order: %s'  % solution.inorderMorris(root)
    print 'post order: %s' % solution.postOrderTraversalNonRecursive(root)
    print 'post order: %s' % solution.postorderMorris(root)
    print 'level order: %s'% solution.levelOrderTraversal(root)
