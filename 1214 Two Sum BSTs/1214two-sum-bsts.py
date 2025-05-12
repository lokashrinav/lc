# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        hset = set()

        def dfs(node):
            if not node:
                return
            hset.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root1)

        def dfs2(node):
            nonlocal target

            if not node:
                return False
            if target - node.val in hset:
                return True

            return dfs2(node.left) or dfs2(node.right)

        return dfs2(root2)    