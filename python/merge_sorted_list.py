#! /usr/bin/python

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.x = x
#         self.next = None

from node_struct import ListNode
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        pivot = ListNode(0)
        cursor = pivot
        cursor1 = l1
        cursor2 = l2
        while cursor1 and cursor2:
            if cursor1.x < cursor2.x:
                cursor.next = cursor1
                cursor1 = cursor1.next
            else:
                cursor.next = cursor2
                cursor2 = cursor2.next
            cursor = cursor.next
        if cursor1:
            cursor.next = cursor1
        else:
            cursor.next = cursor2
        return pivot.next

if __name__ == '__main__':
    solution = Solution()
    head1 = ListNode(-1)
    cursor = head1
    for num in range(1,7,2):
        cursor.next = ListNode(num)
        cursor = cursor.next
    head2 = ListNode(0)
    cursor = head2
    for num in range(2,6,2):
        cursor.next = ListNode(num)
        cursor = cursor.next
    head = solution.mergeTwoLists(head1, head2)
    while head:
        print head.x
        head = head.next
    head = solution.mergeTwoLists(ListNode(2), ListNode(1))
    while head:
        print head.x
        head = head.next   
