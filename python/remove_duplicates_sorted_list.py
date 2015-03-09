#! /usr/bin/python


'''
Problem1:
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Problem 2:
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

'''

from node_struct import ListNode
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return None
        pivot = ListNode(head.x-1)
        pivot.next = head
        cursor = pivot
        while cursor.next:
            if cursor.x == cursor.next.x:
                # Delete next node
                cursor.next = cursor.next.next
            else:
                # Move forward
                cursor = cursor.next
        return pivot.next

    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates2(self, head):
        if head is None:
            return None
        pivot = ListNode(head.x-1)
        pivot.next = head
        cursor = pivot
        while cursor.next and cursor.next.next:
            if cursor.next.x == cursor.next.next.x:
                quick_cursor = cursor.next
                while quick_cursor:
                    if quick_cursor.x != cursor.next.x:
                        break
                    quick_cursor = quick_cursor.next
                cursor.next = quick_cursor
            else:
                cursor = cursor.next
        return pivot.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(1)
    d = ListNode(2)
    e = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = ListNode(3)
    solution = Solution()
    head = solution.deleteDuplicates2(a)
    while head:
        print head.x
        head = head.next
