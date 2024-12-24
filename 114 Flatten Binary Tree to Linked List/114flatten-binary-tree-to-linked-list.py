# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def dfs(node):
            if node and not node.left and not node.right:
                return [node, node]

            if node and node.left:
                leftNode, finalLeft = dfs(node.left)
            else:
                leftNode, finalLeft = None, node

            if node and node.right:
                rightNode, finalRight = dfs(node.right)
            else:
                rightNode, finalRight = None, finalLeft

            node.right = leftNode
            node.left = None
            finalLeft.right = rightNode

            return [node, finalRight]

        return dfs(root)
        