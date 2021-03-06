#! /usr/bin/python

'''
Reverse a linked list

Proiblem 2:
 Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
'''

from node_struct import ListNode
class Solution:
    def reverseList(self, head, tail=None):
        if not head or head.next is None:
            return head
        pre_node = tail
        cursor = head
        next_node = cursor.next
        while cursor.next != tail:
            next = cursor.next
            cursor.next = pre_node
            pre_node = cursor
            cursor = next
        cursor.next = pre_node
        return cursor

    def reverseLength(self, head, n):
        if not head or head.next is None:
            return head
        pre_node = None
        cursor = head
        next_node = cursor.next
        count = 0
        while count < n:
            next = cursor.next
            cursor.next = pre_node
            pre_node = cursor
            cursor = next
            count += 1
        head.next = next
        return pre_node

    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        pivot = ListNode(0)
        pivot.next = head
        count = 0
        cursor = pivot
        while count < m - 1:
            count += 1
            cursor = cursor.next
        first_tail = cursor
        second_tail = cursor.next
        pre_node = None
        while count < n+1:
            next = cursor.next
            cursor.next = pre_node
            pre_node = cursor
            cursor = next
            count += 1
        first_tail.next = pre_node
        second_tail.next = next
        return pivot.next

    def moveCursor(self, cursor, m):
        while cursor and m > 0:
            cursor = cursor.next
            m -= 1
        return cursor

    def reverseBetween2(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        pivot = ListNode(0)
        pivot.next = head
        cursor = pivot
        seg1_tail = self.moveCursor(cursor, m-1)
        seg2_head = seg1_tail.next
        cursor = pivot
        seg3_head = self.moveCursor(cursor, n+1)
        seg1_tail.next = self.reverseList(seg2_head, seg3_head)
        return pivot.next

if __name__ == '__main__':
    list_array = list()
    head = ListNode(1)
    cursor = head
    for index in range(2,11):
        cursor.next = ListNode(index)
        cursor = cursor.next
    solution = Solution()
    new_head = solution.reverseBetween2(head, 1, 4)
    while new_head:
        print new_head.x
        new_head = new_head.next
