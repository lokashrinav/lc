"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':

        def inorder(node):
            if not node:
                return None

            left = inorder(node.left)

            if left:
                return left

            return node
            
        if node.right:
            return inorder(node.right)
        else:
            p = node.parent
            if not p:
                return None
            if p.right == node:
                while p:
                    if not p.parent:
                        return None

                    if p.parent.left == p:
                        return p.parent
                    p = p.parent

                if not p:
                    return None
            else:
                return p        