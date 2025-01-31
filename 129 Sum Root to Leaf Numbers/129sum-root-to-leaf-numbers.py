# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, curr):
            if not node:
                return 0

            curr = curr * 10 + node.val
            
            total = 0

            if not node.left and not node.right:
                return curr
            else:
                total += dfs(node.right, curr)
                total += dfs(node.left, curr)
            
            return total
            
        return dfs(root, 0) 
        