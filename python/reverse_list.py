#! /usr/bin/python

'''
Reverse a linked list
'''

from node_struct import ListNode
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        pre_node = None
        cursor = head
        next_node = cursor.next
        while cursor.next:
            next = cursor.next
            cursor.next = pre_node
            pre_node = cursor
            cursor = next
        cursor.next = pre_node
        return cursor

if __name__ == '__main__':
    list_array = list()
    head = ListNode(0)
    cursor = head
    for index in range(1,10):
        cursor.next = ListNode(index)
        cursor = cursor.next
    solution = Solution()
    new_head = solution.reverseList(head)
    while new_head:
        print new_head.x
        new_head = new_head.next
