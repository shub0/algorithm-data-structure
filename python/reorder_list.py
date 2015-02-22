#! /usr/bin/python

'''
Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln->Ln-1->L2->Ln-2->...
You must do this in-place without altering the nodes' values.
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

from node_struct import ListNode
class Solution:
    # @param head, a ListNode
    # @return a integer
    @classmethod
    def getSize(cls, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        length = Solution.getSize(head)
        if length < 3:
            return head
        second_head = head
        # move to the second half of linked list
        move_count = length / 2
        while move_count > 0:
            move_count -= 1
            second_head = second_head.next
        # reverse the second half of linked list
        pre_node = second_head
        cursor_node = second_head.next
        second_head.next = None
        next_node = cursor_node.next
        while cursor_node.next:
            next_node = cursor_node.next
            cursor_node.next = pre_node
            pre_node = cursor_node
            cursor_node = next_node
        cursor_node.next = pre_node
        
        # zip the first half and second half
        pivot = head
        move_count = length / 2
        while move_count > 0:
            move_count -= 1
            pre_node = cursor_node.next
            next_node = pivot.next
            pivot.next = cursor_node
            cursor_node.next = next_node
            cursor_node = pre_node
            pivot = next_node
        pivot.next = None
        return head

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
