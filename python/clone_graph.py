#! /usr/bin/python

'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from node_struct import UndirectedGraphNode
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        self.node_dict = dict()
        return self.createNode(node)

    # depth-first search
    def createNode(self, node):
        new_node = UndirectedGraphNode(node.label)
        self.node_dict[new_node.label] = new_node
        for neighbor in node.neighbors:
            if neighbor.label not in self.node_dict:
                self.createNode(neighbor)
            new_node.neighbors.append(self.node_dict[neighbor.label])
        return new_node

    # breath-with search
    def printGraph(self, node):
        visited = set()
        queue   = [node]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.label in visited:
                continue
            visited.add(node.label)
            queue += [ neighbor for neighbor in node.neighbors if neighbor.label not in visited ]
        return visited

if __name__ == '__main__':
    solution = Solution()
    node_1 = UndirectedGraphNode(1)
    node_2 = UndirectedGraphNode(2)
    node_3 = UndirectedGraphNode(3)
    node_1.neighbors = [node_2, node_3]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_1, node_2, node_3]
    new_node_1 = solution.cloneGraph(node_1)
    print solution.printGraph(new_node_1)
