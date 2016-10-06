'''
Given a singly linked list, determine if it is a palindrome.
'''

class Solution(object):
    def reverse(self, head):
        if (not head) or (not head.next):
            return head
        prev = None
        curr = head
        next = None
        while curr.next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr.next = prev
        return curr

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (not head) or (not head.next):
            return True
        slow = head
        quick = head
        while (quick.next and quick.next.next):
            slow = slow.next
            quick = quick.next.next
        new_head = slow.next
        slow.next = None
        new_cursor = self.reverse(new_head)
        cursor = head
        while cursor and new_cursor:
            if cursor.val != new_cursor.val:
                return False
            cursor = cursor.next
            new_cursor = new_cursor.next
        return True
