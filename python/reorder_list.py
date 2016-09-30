#! /usr/bin/python

'''
Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln->Ln-1->L2->Ln-2->...
You must do this in-place without altering the nodes' values.
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

from node_struct import ListNode
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if (not head):
            return None
        quick_cursor = head
        slow_cursor = head
        while (quick_cursor and quick_cursor.next):
            quick_cursor = quick_cursor.next.next
            slow_cursor = slow_cursor.next
        sec_head = slow_cursor.next
        slow_cursor.next = None
        new_head = self.reverse(sec_head)
        self.zip(head, new_head)

    def zip(self, head1, head2):
        pivot = ListNode(0)
        pivot.next = head1
        cursor = pivot
        while (head1 or head2):
            if head1:
                cursor.next=head1
                cursor = cursor.next
                head1 = head1.next
            if head2:
                cursor.next=head2
                cursor = cursor.next
                head2 = head2.next
        return pivot.next

    def reverse(self, head):
        if (not head or not head.next):
            return head
        prev = None
        curr = head
        next = head.next
        while curr.next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr.next = prev
        return curr


if __name__ == '__main__':
    list_array = list()
    head = ListNode(0)
    cursor_node = head
    for index in range(1,5):
        cursor_node.next = ListNode(index)
        cursor_node = cursor_node.next
    solution = Solution()
    new_head = solution.reorderList(head)
    while new_head:
        print new_head.x
        new_head = new_head.next
