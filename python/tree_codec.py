'''
Serialize and Deserialize Binary Tree  QuestionEditorial Solution  My Submissions
Total Accepted: 32879
Total Submissions: 108712
Difficulty: Hard
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from node_struct import TreeNode
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        cursor = root
        output = []
        nodes_in_tree = deque()
        nodes_in_tree.append(cursor)
        while len(nodes_in_tree) > nodes_in_tree.count(None):
            node = nodes_in_tree.popleft()
            output.append(node)
            if node:
                nodes_in_tree.append(node.left)
                nodes_in_tree.append(node.right)
        return "[" + ",".join([ str(node.val) if node else "null" for node in output ]) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if not data:
            return None
        num = data.split(",")
        size = len(num)
        nodes = map(lambda x: TreeNode(int(x)) if x != "null" else None, num)
        missing = 0
        for (index, node) in enumerate(nodes[:size]):
            left_index = 2 * index + 1 - 2 * missing
            right_index = 2 * index + 2 - 2 * missing
            if not node:
                missing += 1
            if node and left_index < size:
                node.left = nodes[left_index]
            if node and right_index < size:
                node.right = nodes[right_index]
        return nodes[0]

# Your Codec object will be instantiated and called as such:
codec = Codec()
data = "[-1,0,1]"
root = codec.deserialize(data)
print root.val
print codec.serialize(root)
# print codec.deserialize(codec.serialize(root))
