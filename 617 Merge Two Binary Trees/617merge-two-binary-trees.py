# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if not node2 and not node1:
                return None
            elif node2 and not node1:
                return node2
            elif node1 and not node2:
                return node1

            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return TreeNode(node1.val + node2.val, left, right)

        return dfs(root1, root2)