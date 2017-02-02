#! /usr/bin/python

'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

from node_struct import ListNode, TreeNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getSize(self, head):
        cursor = head
        size = 0
        while cursor:
            size += 1
            cursor = cursor.next
        return size

    def moveNode(self, head, k):
        cursor = head
        while cursor and k > 0:
            cursor = cursor.next
            k -= 1
        return cursor

    def _sortedListToBST(self, head, size):
        if not head:
            return None
        if size == 1:
            return TreeNode(head.val)
        if size == 2:
            root = TreeNode(head.val)
            root.right = TreeNode(head.next.val)
            return root
        left_head = head
        left_size = (size-1)/2
        left_tail = self.moveNode(left_head, left_size-1)
        root_node = left_tail.next
        right_head = root_node.next
        left_tail.next = None
        root_node.next = None
        root = TreeNode(root_node.val)
        root.left = self._sortedListToBST(left_head, left_size)
        root.right = self._sortedListToBST(right_head, size-1-left_size)
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        size = self.getSize(head)
        return self._sortedListToBST(head, size)

if __name__ == '__main__':
    head = ListNode(1)
    cursor = head
    for index in range(2,5):
        cursor.next = ListNode(index)
        cursor = cursor.next

    solution = Solution()
    root = solution.sortedListToBST(head)
    print root.val, root.left.val, root.right.val
