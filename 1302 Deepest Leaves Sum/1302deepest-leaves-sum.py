# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node, leng):
            if not node:
                return (None, leng)
            
            if not node.left and not node.right:
                return (node.val, leng)

            length1, length2 = 0, 0
            if node.left:
                left, length1 = dfs(node.left, leng + 1)

            if node.right:
                right, length2 = dfs(node.right, leng + 1)

            if length1 > length2:
                return (left, length1)
            elif length2 > length1:
                return (right, length2)
            else:
                return (left + right, length1)
            
        curr, val = dfs(root, 0)

        return curr