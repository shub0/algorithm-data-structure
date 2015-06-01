#! /usr/bin/python

'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

from node_struct import ListNode

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        pivot = ListNode(0)
        pivot.next = head
        cursor = pivot
        while cursor.next and cursor.next.next:
            node1 = cursor.next
            node2 = cursor.next.next
            node3 = cursor.next.next.next
            # swap pairs
            cursor.next = node2
            node2.next = node1
            # link to next node
            node1.next = node3
            # move forward
            cursor = node1
        return pivot.next

if __name__ == '__main__':
    list_array = list()
    head = ListNode(0)
    cursor_node = head
    for index in range(1,2):
        cursor_node.next = ListNode(index)
        cursor_node = cursor_node.next
        solution = Solution()
        new_head = solution.swapPairs(head)
        while new_head:
            print new_head.x
            new_head = new_head.next
