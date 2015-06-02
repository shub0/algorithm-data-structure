#! /usr/bin/python

'''
Convert a sorted double linked list to a balanced BST
Convert a BST to a sorted double linked list
'''

from node_struct import TreeNode, DoubleListNode
class Solution:
    def BST2DoubleList(self, root):
        if not root.left and not root.right:
            return root
        else:
            new_head = root
            if root.left:
                left_head = self.BST2DoubleList(root.left)
                new_head = left_head
                while left_head.right:
                    left_head = left_head.right
                left_head.right = root
                root_left = left_head
            if root.right:
                right_head = self.BST2DoubleList(root.right)
                root.right = right_head
                right_head.left = root
        return new_head

    def getLength(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.right
        return count

    def DoubleList2BST(self, head):
        length = self.getLength(head)
        return self.DoubleList2BSTRecursive(head, length)

    def getKthNode(self, head, k):
        curr = head
        while k > 0:
            k -= 1
            curr = head.right
        return curr

    def DoubleList2BSTRecursive(self, head, length):
        if length <= 0:
            return None
        if length == 1:
            return head
        left_length = length / 2
        left_tail = self.getKthNode(head, left_length - 1)
        root = left_tail.right
        left_tail.right = None
        right_head = root.right
        root.right = None
        root.left = self.DoubleList2BSTRecursive(head, length / 2)
        root.right = self.DoubleList2BSTRecursive(right_head, length - left_length - 1)
        return root

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    head = solution.BST2DoubleList(root)
    new_root = solution.DoubleList2BST(head)
    print new_root.val
