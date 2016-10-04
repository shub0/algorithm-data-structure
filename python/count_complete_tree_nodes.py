'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (not root):
            return 0
        curr = root
        count = 1
        while curr.left:
            if (self.getHeight(curr.left) > self.getHeight(curr.right)):
                curr = curr.left
                count *= 2
            else:
                curr = curr.right
                count = count * 2 + 1
        return count

    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height
