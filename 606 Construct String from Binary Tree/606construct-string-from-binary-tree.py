# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if not node:
                return ""
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left or right:
                left = "(" + left + ")"
            if right:
                right = "(" + right + ")"

            str1 = str(node.val) + left + right

            return str1
        
        return dfs(root)
        