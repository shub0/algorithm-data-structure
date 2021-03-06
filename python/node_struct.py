class ListNode:
    def __init__(self, x):
        self.x = x
        self.val = x
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

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# Definition for a TreeNode
class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None

# Defintion for a TreeLinkNode
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
