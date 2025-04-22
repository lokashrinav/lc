# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        
        def helper(node, idk):
            if not node:
                return None
            
            if depth - 1 == idk:
                newNode1 = TreeNode(val)
                newNode2 = TreeNode(val)
                newNode1.left = node.left
                newNode2.right = node.right
                node.left = newNode1
                node.right = newNode2
                return node
                    
            left = helper(node.left, idk + 1)
            right = helper(node.right, idk + 1)

            node.left = left
            node.right = right

            return node
        
        return helper(root, 1)

        
