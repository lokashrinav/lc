# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        saved = None
        saved2 = None
        def find(node, parent):
            nonlocal saved, saved2

            if not node:
                return False
            
            if node.val == x:
                saved = parent
                saved2 = node
                return True
            
            return find(node.left, node) or find(node.right, node)

        find(root, None)

        def dfs(node, curr):
            if not node:
                return 0
            
            if node.val == curr:
                return 0
            
            return 1 + dfs(node.left, curr) + dfs(node.right, curr)

        if saved is not None:
                
            count1 = dfs(root, x)
            count2 = dfs(saved2, -1)

            if count1 > count2:
                return True
         
        count0 = dfs(root, x)
        count1 = dfs(saved2.right, x)
        count2 = dfs(saved2.left, x)

        if count0 + count1 + 1 < count2 or count0 + count2 + 1 < count1:
            return True

        return False

