#! /usr/bin/python

'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

from node_struct import ListNode
class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        pivot_small = ListNode(0)
        pivot_large = ListNode(0)
        curr_node = head
        small_node = pivot_small
        large_node = pivot_large
        while curr_node:
            if curr_node.val < x:
                small_node.next = curr_node
                small_node = small_node.next
            else:
                large_node.next = curr_node
                large_node = large_node.next
            curr_node = curr_node.next
        small_node.next = pivot_large.next
        large_node.next = None
        return pivot_small.next

if __name__ == '__main__':
    head = ListNode(10)
    cursor = head
    for index in range(9, 1, -1):
        cursor.next = ListNode(index)
        cursor = cursor.next
    cursor = head

    solution = Solution()
    new_head = solution.partition(head, 7)
    while new_head:
        print new_head.val
        new_head = new_head.next
