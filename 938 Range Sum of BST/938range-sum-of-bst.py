# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            if node.val > high:
                left = dfs(node.left)      
                return left  
            elif node.val < low:
                right = dfs(node.right)
                return right
            elif node.val >= low and node.val <= high:
                return dfs(node.left) + dfs(node.right) + node.val
            
            return 0

        return dfs(root)

        