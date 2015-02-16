#! /usr/bin/python

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
'''

from node_struct import ListNode
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        fast_node = head
        slow_node = head
        while (fast_node.next and fast_node.next.next):
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if fast_node == slow_node:
                break
        if fast_node.next is None or fast_node.next.next is None:
            return False
        return True

    def get_size(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        fast_node = head
        slow_node = head
        while (fast_node.next and fast_node.next.next):
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                break
        if fast_node.next is None or fast_node.next.next is None:
            return None
        fake_head = fast_node.next
        fast_node.next = None
        orig_len = self.get_size(head)
        fake_len = self.get_size(fake_head)
        # in case the list is a whole cycle and size = 2
        if orig_len == 1:
            return head
        if orig_len > fake_len:
            diff_len = orig_len - fake_len
            while diff_len > 0:
                head = head.next
                diff_len -= 1
        else:
            diff_len = orig_len - fake_len
            while diff_len > 0:
                fake_head = fake_head.next
                diff_len -= 1
        while head and fake_head:
            if head == fake_head:
                return head
                head = head.next
                fake_head = fake_head.next
        

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = a
    b.next = c
    c.next = d
    d.next = b
    solution = Solution()
    print solution.detectCycle(a).x
