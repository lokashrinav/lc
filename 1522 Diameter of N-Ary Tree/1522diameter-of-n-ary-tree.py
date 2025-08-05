"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        maxLen = 0
        def dfs(node):
            nonlocal maxLen

            if not node:
                return 0

            max1 = 0
            max2 = 0
            for elem in node.children:
                calc = dfs(elem)
                if calc > max1:
                    max2 = max1
                    max1 = calc
                elif calc > max2:
                    max2 = calc
                
            maxLen = max(maxLen, max1 + max2 + 1)
            
            return 1 + max1

        dfs(root)

        return maxLen - 1