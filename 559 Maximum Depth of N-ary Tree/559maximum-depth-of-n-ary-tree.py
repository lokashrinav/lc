"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0
        
        total = 1

        for child in root.children:
            total = max(total, 1 + self.maxDepth(child))
        
        return total
        