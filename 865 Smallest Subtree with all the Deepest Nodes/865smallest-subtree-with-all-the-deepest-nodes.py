# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, curr):
            if not node:
                return (curr - 1, None)

            if not node.left and not node.right:
                return (curr, node)

            val1, node2 = dfs(node.left, curr + 1)
            val2, node3 = dfs(node.right, curr + 1)

            if val1 == val2:
                return (val1, node)
            elif val1 > val2:
                return (val1, node2)
            else:
                return (val2, node3)

        return dfs(root, 0)[1]
        