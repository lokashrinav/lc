"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        lis = []
        def dfs(node):
            if not node:
                return None
            for child in node.children:
                dfs(child)
            lis.append(node.val)
            return None
            
        dfs(root)
        return lis