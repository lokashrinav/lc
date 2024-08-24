# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        bool1 = [False]
        def check(node, val):
            if not node:
                return
            val += node.val
            if (not node.right and not node.left) and val == targetSum:
                bool1[0] = True
            check(node.right, val)
            check(node.left, val)

        check(root, 0)

        return bool1[0]        