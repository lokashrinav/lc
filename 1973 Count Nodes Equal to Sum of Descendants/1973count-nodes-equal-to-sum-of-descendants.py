# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:

        total = 0
        def dfs(node):
            nonlocal total
            if not node:
                return 0
            
            calc1 = dfs(node.left)
            calc2 = dfs(node.right)

            if calc1 + calc2 == node.val:
                total += 1

            return calc1 + calc2 + node.val

        dfs(root)

        return total
        