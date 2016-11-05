'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

from node_struct import TreeNode
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0.0, 0.0
            else:
                rob_root_l, root_l = dfs(root.left)
                rob_root_r, root_r = dfs(root.right)
                rob_root = max(root.val + root_l + root_r, rob_root_l + rob_root_r)
                rob = rob_root_r + rob_root_l
                return rob_root, rob
        return dfs(root)[0]
