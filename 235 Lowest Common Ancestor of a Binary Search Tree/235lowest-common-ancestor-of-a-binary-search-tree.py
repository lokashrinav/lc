# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cache = [0]
        def dfs(node):
            if not node:
                return 0

            saved_num = 0

            if node.val == p.val:
                saved_num = 1
            if node.val == q.val:
                saved_num = 2

            left_saved = dfs(node.left)

            if left_saved == 3:
                return 0
                
            right_saved = dfs(node.right)

            if right_saved == 3:
                return 0

            if left_saved + right_saved == 3:
                cache[0] = node
                return 0

            if saved_num + left_saved + right_saved == 3:
                cache[0] = node
                return 0
            
            return saved_num + left_saved + right_saved
        dfs(root)
        return cache[0]
        