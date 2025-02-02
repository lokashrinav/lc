# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, x):
            if not node:
                return 0
            
            if not node.left and not node.right and x == -1:
                return node.val

            return dfs(node.left, -1) + dfs(node.right, 1)          
        
        return dfs(root, 0)
        