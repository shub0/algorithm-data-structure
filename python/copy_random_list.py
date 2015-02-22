#! /usr/bin/python

'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
'''

from node_struct import RandomListNode
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        # step 1:
        # Create a list as A->A*->B->B*->C->C*->...
        pivot = head
        while pivot:
            copy_node = RandomListNode(pivot.label)
            next_node = pivot.next
            pivot.next = copy_node
            copy_node.next = next_node
            pivot = next_node
        # Step 2:
        # Link random pointer
        pivot = head
        while pivot:
            copy_node = pivot.next
            random_node = pivot.random
            if random_node:
                copy_node.random = random_node.next
            pivot = copy_node.next
        # Step 3: unzip the linked list
        # Create a List A*->B*->C*->...
        # Restore origin list as A->B->C->...
        pivot = head
        new_head = head.next
        while pivot.next.next:
            copy_node = pivot.next
            next_node = copy_node.next
            next_copy_node = next_node.next
            pivot.next = next_node
            copy_node.next = next_copy_node
            pivot = pivot.next
        pivot.next = None
        return new_head

if __name__ == '__main__':
    head = RandomListNode(0)
    cursor_node = head
    for index in range(1,5):
        cursor_node.next = RandomListNode(index)
        cursor_node = cursor_node.next
    head.random = head.next.next
    solution = Solution()
    new_head = solution.copyRandomList(head)
    print new_head.random.label
    while new_head:
        print new_head.label
        new_head = new_head.next
