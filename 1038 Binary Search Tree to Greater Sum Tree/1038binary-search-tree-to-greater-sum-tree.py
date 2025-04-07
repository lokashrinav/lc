# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        saved = 0
        def dfs(node):
            nonlocal saved

            if not node:
                return
            
            dfs(node.right)
            prev = node.val
            node.val += saved
            saved += prev
            dfs(node.left)

        dfs(root)

        return root
