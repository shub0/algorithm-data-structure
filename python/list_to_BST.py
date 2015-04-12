#! /usr/bin/python

'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

from node_struct import ListNode, TreeNode
class Solution:
    def _listLen(self, head):
        cursor = head
        len = 0
        while cursor:
            len += 1
            cursor = cursor.next
        return len

    # Assume index < list_len, no error check
    def _getListNode(self, head, index):
        cursor = head
        while index > 0 and cursor:
            index -= 1
            cursor = cursor.next
        return cursor

    def _sortedListToBST(self, head, list_len):
        if not head:
            return None
        if list_len == 1:
            return TreeNode(head.val)
        left_head = head
        left_length = list_len / 2
        left_tail = self._getListNode(head, left_length-1)
        root_node = left_tail.next
        left_tail.next = None
        right_head = root_node.next
        root_node.next = None
        root = TreeNode(root_node.val)
        root.left = self._sortedListToBST(left_head, left_length)
        root.right = self._sortedListToBST(right_head, list_len - 1 - left_length)
        return root

    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return None
        list_len = self._listLen(head)
        if list_len == 1:
            return TreeNode(head.val)
        return self._sortedListToBST(head, list_len)

if __name__ == '__main__':
    head = ListNode(1)
    cursor = head
    for index in range(2,5):
        cursor.next = ListNode(index)
        cursor = cursor.next

    solution = Solution()
    root = solution.sortedListToBST(head)
    print root.val, root.left.val, root.right.val
