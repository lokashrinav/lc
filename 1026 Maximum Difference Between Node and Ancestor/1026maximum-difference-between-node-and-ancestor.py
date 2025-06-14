# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        maxDiff = 0
        def dfs(node, smallest):
            nonlocal maxDiff

            if not node:
                return
            
            maxDiff = max(node.val - smallest, maxDiff)

            dfs(node.left, min(smallest, node.val))
            dfs(node.right, min(smallest, node.val))

        def dfs2(node, biggest):
            nonlocal maxDiff

            if not node:
                return
            
            maxDiff = max(biggest - node.val, maxDiff)

            dfs2(node.left, max(biggest, node.val))
            dfs2(node.right, max(biggest, node.val))

        dfs(root, root.val)
        dfs2(root, root.val)

        return maxDiff


        