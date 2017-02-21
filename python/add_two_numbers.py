# You are given two linked lists representing two non-negative numbers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_struct import ListNode
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = list()
        s2 = list()
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        sum = 0
        res = None
        total = 0
        while s1 or s2:
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            new = ListNode(total % 10)
            new.next = res
            res = new
            total /= 10

        if total >= 10:
            new = ListNode(total/10)
            res.next = new
            res = new
        return res

solution = Solution()
node1 = ListNode(1)
node1.next = ListNode(3)

print solution.addTwoNumbers(node1, ListNode(9)).val
