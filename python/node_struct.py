class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None

class PointNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None