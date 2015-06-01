#! /usr/bin/python

'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''


from node_struct import ListNode


class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        pivot = ListNode(0)
        pivot.next = head
        fast_node = pivot
        while n > 0:
            fast_node = fast_node.next
            n -= 1
        slow_node = pivot
        while fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next
        slow_node.next = slow_node.next.next

        return pivot.next

if __name__ == '__main__':
    list_array = list()
    head = ListNode(1)
    cursor_node = head
    for index in range(2,10):
        cursor_node.next = ListNode(index)
        cursor_node = cursor_node.next
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, 9)
    while new_head:
        print new_head.x
        new_head = new_head.next
