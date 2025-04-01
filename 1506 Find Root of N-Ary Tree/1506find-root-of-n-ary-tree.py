"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for child in node.children:
                dfs(child)


        visited = set()
        curr = None
        for node in tree:
            if node not in visited:
                dfs(node)
                curr = node

        return curr
        