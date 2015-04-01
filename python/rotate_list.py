#! /usr/bin/python

'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

from node_struct import ListNode
class Solution:
    # @param head, a ListNode
    # @return an integer
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        pivot = ListNode(0)
        pivot.next = head
        quick_cursor = pivot
        size = self.getLength(head)
        if size == 0:
            return head

        k = k % size
        while k > 0:
            quick_cursor = quick_cursor.next
            if not quick_cursor:
                quick_cursor = pivot.next
            k -= 1
        cursor = pivot
        while quick_cursor.next:
            quick_cursor = quick_cursor.next
            cursor = cursor.next
        quick_cursor.next = pivot.next
        pivot.next = cursor.next
        cursor.next = None
        return pivot.next

if __name__ == '__main__':
    head = ListNode(1)
    cursor = head
    for index in range(2,6):
        cursor.next = ListNode(index)
        cursor = cursor.next
    solution = Solution()
    new_head = solution.rotateRight(head, 4)
    while new_head:
        print new_head.x
        new_head = new_head.next
