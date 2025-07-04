# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def dfs(node, curr):
            if not node:
                return curr < limit

            curr += node.val

            first = second = True

            if node.left:
                first = dfs(node.left, curr)
            
            if node.right:
                second = dfs(node.right, curr) 
            
            if not node.left and not node.right:
                first = dfs(node.left, curr)
                second = dfs(node.right, curr) 

            if first and second:
                return True
            elif first:
                node.left = None
            elif second:
                node.right = None

            return False
                   
        final = dfs(root, 0)

        if final:
            return None
        
        return root
        