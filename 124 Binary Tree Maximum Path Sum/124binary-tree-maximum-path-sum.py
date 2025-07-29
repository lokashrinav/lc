# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxNum = float('-inf')
        def dfs(node):
            nonlocal maxNum
            if not node:
                return float('-inf')
            
            left, right = dfs(node.left), dfs(node.right)

            maxNum = max(maxNum, node.val + left + right, node.val, node.val + left, node.val + right)

            curr = node.val + (max(left, right) if max(left, right) >= 0 else 0)
            
            return max(curr, 0)
        
        dfs(root)

        return maxNum
        