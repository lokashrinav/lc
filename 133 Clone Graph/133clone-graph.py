"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        hmap = {}
        def dfs(node):
            if not node:
                return None

            if node.val in hmap:
                return hmap[node.val]

            newNode = Node(node.val, [])
            hmap[node.val] = newNode

            newNode.neighbors = []
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))

            return newNode

        return dfs(node)
        