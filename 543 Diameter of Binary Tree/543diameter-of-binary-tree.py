# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxNum = [0]

        def dfs(node, curr):
            if not node:
                return 0 
            
            right = dfs(node.right, curr + 1)
            left = dfs(node.left, curr + 1)

            curr = 1 + right + left

            maxNum[0] = max(maxNum[0], curr)

            return max(left + 1, right + 1)

        dfs(root, 0)

        return maxNum[0] - 1
        