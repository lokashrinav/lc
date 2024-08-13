# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def dfs(node, value):
            if not node:
                return 0
            if node.val >= value:
                print(node.val)
                count[0] += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, value)
                dfs(node.right, value) 

        dfs(root, float('-inf'))

        return count[0]
        