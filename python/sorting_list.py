#! /usr/bin/python


from node_struct import ListNode

class Solution:
    # @param head, a listnode
    # @return a listnode
    # sort a linked list in o(n log n) time using constant space complexity.
    def sortList(self, head):
        if (head is None) or (head.next is None):
            return head
        fast_head = head
        slow_head = head
        while (fast_head.next and fast_head.next.next):
            fast_head = fast_head.next.next
            slow_head = slow_head.next
        
        pivot_first  = head
        pivot_second = slow_head.next
        slow_head.next = None
        pivot_first = self.sortList(pivot_first)
        pivot_second = self.sortList(pivot_second)
        return self.merge(pivot_first, pivot_second)

    def merge(self, head1, head2):
        if (head1 is None):
            return head2
        if (head2 is None):
            return head1
        if (head1 == head2):
            return head1
        head = ListNode(0)
        pivot = head
        while (head1 and head2):
            if (head1.x > head2.x):
                pivot.next = head2
                head2 = head2.next
            else:
                pivot.next = head1
                head1 = head1.next
            pivot = pivot.next
        if (head1 is None):
            pivot.next = head2
        else:
            pivot.next = head1
        return head.next

    # @param head, a ListNode
    # @return a ListNode
    # Sort a linked list using insertion sort.
    def insertionSortList(self, head):
        if head is None:
            return head
        fake_head = ListNode(0)
        fake_head.next = head
        cursor = head.next
        tail = head
        while cursor is not None:
            if cursor.x < tail.x:
                tmp_node = fake_head.next
                # insert before head
                if cursor.x < tmp_node.x:
                    tail.next = cursor.next
                    cursor.next = fake_head.next
                    fake_head.next = cursor
                # search for insertion position and then insert
                else:
                    while tmp_node.next is not None:
                        if cursor.x >= tmp_node.x and cursor.x < tmp_node.next.x:
                            tail.next = cursor.next
                            cursor.next = tmp_node.next
                            tmp_node.next = cursor
                            break
                        tmp_node = tmp_node.next
                cursor = tail.next
            else:
                tail = cursor
                cursor = cursor.next
        return fake_head.next

if __name__ == '__main__':
    head1 = ListNode(5)
    head2 = ListNode(4)
    head2.next = ListNode(6)
    head2.next.next = ListNode(1)
    head1.next = head2
    solution = Solution()
    node = solution.insertionSortList(head1)
    while (node):
        print node.x
        node = node.next
