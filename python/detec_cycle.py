#! /usr/bin/python

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
'''

from node_struct import ListNode
class Solution:
    # @param head, a ListNode
    # @return a boolean
   def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (not head):
            return False
        quick_cursor = head
        slow_cursor = head
        while (quick_cursor and quick_cursor.next):
            quick_cursor = quick_cursor.next.next
            slow_cursor = slow_cursor.next
            if (quick_cursor == slow_cursor):
                return True
        return False
    def getSize(self, head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head):
            return None
        quick_cursor = head
        slow_cursor = head
        while (quick_cursor and quick_cursor.next):
            quick_cursor = quick_cursor.next.next
            slow_cursor = slow_cursor.next
            if (quick_cursor == slow_cursor):
                break
        # No cycle
        if (not quick_cursor) or (not quick_cursor.next):
            return None
        new_cursor = quick_cursor.next
        quick_cursor.next = None
        cursor = head
        size1 = self.getSize(cursor)
        size2 = self.getSize(new_cursor)
        # Align head
        while size1 > size2:
            cursor = cursor.next
            size1 -= 1
        while size2 > size1:
            new_cursor = new_cursor.next
            size2 -= 1

        while cursor and new_cursor:
            if cursor == new_cursor:
                return cursor
            cursor = cursor.next
            new_cursor = new_cursor.next
        return None


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
