"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        prev = [Node(0)]
        first = []
        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            if not left and not first:
                first.append(node)
                
            prev[0].right = node
            node.left = prev[0]
            prev[0] = node
            right = dfs(node.right)

            return 1

        dfs(root)

        print(first[0].val)
        print(prev[0].val)

        prev[0].right = first[0]
        first[0].left = prev[0]

        return first[0]
        


        