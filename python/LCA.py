'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself)"
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''

from node_struct import TreeNode
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root == q) or (root == p) or (not root):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root

    def LCA(self, root, p, q):
        nodes_in_tree = [root]
        tree = {root: None}
        while p not in tree or q not in tree:
            node = nodes_in_tree.pop()
            if node.left:
                tree[node.left] = node
                nodes_in_tree.append(node.left)
            if node.right:
                tree[node.right] = node
                nodes_in_tree.append(node.right)
        ancestor = []
        while p:
            ancestor.append(p)
            p = tree[p]
        while q not in ancestor:
            q = tree[q]
        return q

solution = Solution()
root = TreeNode(1)
p = TreeNode(4)
q = TreeNode(8)
root.left = TreeNode(2)
root.left.left = p
root.right = TreeNode(3)
root.right.right = q
path = solution.LCA(root, p,q)
print path.val
