#! /usr/bin/python


'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
For example,
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
'''

from node_struct import ListNode

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        pivot = ListNode(0)
        pivot.next = head
        curr_node = pivot
        while curr_node.next:
            tail = self.moveKNode(curr_node, k)
            if not tail:
                break
            new_head = tail.next
            tail.next = None
            curr_node.next = self.reverse(curr_node.next)
            curr_node = self.moveKNode(curr_node, k)
            curr_node.next = new_head
        return pivot.next

    def moveKNode(self, head, k):
        curr_node = head
        while k > 0 and curr_node:
            k -= 1
            curr_node = curr_node.next
        return curr_node

    def reverse(self, head):
        if not head or not head.next:
            return head
        prev_node = None
        curr_node = head
        next_node = head.next
        while next_node:
            curr_node.next = prev_node
            prev_node, curr_node, next_node = curr_node, next_node, next_node.next
        curr_node.next = prev_node
        return curr_node

if __name__ == '__main__':
    list_array = list()
    head = ListNode(1)
    cursor_node = head
    for index in range(2,10):
        cursor_node.next = ListNode(index)
        cursor_node = cursor_node.next
    solution = Solution()
    new_head = solution.reverseKGroup(head, 3)
    while new_head:
        print new_head.x
        new_head = new_head.next
