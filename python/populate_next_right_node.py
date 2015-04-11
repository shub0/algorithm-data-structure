#! /usr/bin/python

'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
        1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

Follow up:
How about the tree is not a perfect binary tree:
For example
Given the following binary tree,
        1
       / \
      2   3
     / \   \
    4   5   7
   /       / \
  8       9   10
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
   /        / \
  8------->9->10->NULL
'''
# The following can handle both cases
from node_struct import TreeLinkNode
class Solution:
    def findNext(self, root):
        cursor = root.next
        while cursor:
            if cursor.left:
                return cursor.left
            elif cursor.right:
                return cursor.right
            cursor = cursor.next
        return None

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        level_head = root
        while level_head:
            cursor = level_head
            level_head = None
            while cursor:
                if cursor.left:
                    # connect children nodes
                    if cursor.right:
                        cursor.left.next = cursor.right
                    else:
                        cursor.left.next = self.findNext(cursor)
                    # Find next level head
                    if not level_head:
                        level_head = cursor.left
                if cursor.right:
                    cursor.right.next = self.findNext(cursor)
                    if not level_head:
                        level_head = cursor.right
                # move to next node
                cursor = cursor.next

if __name__ == '__main__':
    solution = Solution()
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
#    root.right.left = TreeLinkNode(6)
    root.right.right = TreeLinkNode(7)
    root.left.left.left = TreeLinkNode(8)
    root.right.right.left = TreeLinkNode(9)
    root.right.right.right = TreeLinkNode(10)
    solution.connect(root)
    cursor = root
    while cursor:
        head = cursor
        level = list()
        while head:
            level.append(head.val)
            head = head.next
        print level
        while cursor and not cursor.left and not cursor.right:
            cursor = cursor.next
        if not cursor:
            break
        elif cursor.left:
            cursor = cursor.left
        elif cursor.right:
            cursor = cursor.right
