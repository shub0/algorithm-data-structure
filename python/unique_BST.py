#! /usr/bin/python

'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

from node_struct import TreeNode
class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0:
            return 0
        num_BST = [0] * (n+1)
        num_BST[0] = 1
        num_BST[1] = 1
        for index in range(2, n+1):
            for root in range(1, index+1):
                left_tree = root - 1
                right_tree = index - root
                num_BST[index] += num_BST[left_tree]*num_BST[right_tree]
        return num_BST[-1]

    def generateTrees(self, n):
        output = list()
        if n == 0:
            output.append(None)
        return self.generateTreesRecursive(1, n)

    def generateTreesRecursive(self, start, end):
        tree_list = list()
        for root in range(start, end+1):
            left_tree_list = self.generateTreesRecursive(start, root-1)
            right_tree_list = self.generateTreesRecursive(root+1, end)
            left_tree_size = len(left_tree_list)
            right_tree_size = len(right_tree_list)
            if left_tree_size == 0 and right_tree_size == 0:
                tree_list.append(TreeNode(root))
            elif left_tree_size == 0:
                for tree in right_tree_list:
                    root_node = TreeNode(root)
                    root_node.right = tree
                    tree_list.append(root_node)
            elif right_tree_size == 0:
                for tree in left_tree_list:
                    root_node = TreeNode(root)
                    root_node.left = tree
                    tree_list.append(root_node)
            else:
                for left_tree in left_tree_list:
                    for right_tree in right_tree_list:
                        root_node = TreeNode(root)
                        root_node.left = left_tree
                        root_node.right = right_tree
                        tree_list.append(root_node)
        return tree_list


    def copyTree(self, root, base):
        if not root:
            return root
        new_root = TreeNode(root.val + base)
        new_root.left = self.copyTree(root.left, base)
        new_root.right = self.copyTree(root.right, base)
        return new_root

    def generateTrees2(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 0:
            return []
        dp = [ [] for _ in range(n+1) ]
        dp[0].append(None)
        for index in range(1, n+1):
            for mid in range(1,index+1):
                for left_tree in dp[mid-1]:
                    for right_tree in dp[index-mid]:
                        root = TreeNode(mid)
                        root.left = self.copyTree(left_tree, 0)
                        root.right = self.copyTree(right_tree, mid)
                        dp[index].append(root)
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    for index in range(0,10):
        tree_list = solution.generateTrees2(index)
        print 'n = %d, expected %d, got %d' % (index, len(tree_list), solution.numTrees(index))
