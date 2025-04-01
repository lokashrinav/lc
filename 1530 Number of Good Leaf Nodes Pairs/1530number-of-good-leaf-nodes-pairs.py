# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        
        saved = 0
        def dfs(node):
            nonlocal saved

            if not node:
                return []
            
            if node.left is None and node.right is None:
                return [0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            for i in range(len(left)):
                left[i] += 1
            
            for i in range(len(right)):
                right[i] += 1

            if left:
                for i in range(len(left)):
                    for p in range(len(right)):
                        if left[i] + right[p] <= distance:
                            saved += 1
            elif right:
                for i in range(len(right)):
                    for p in range(len(left)):
                        if left[p] + right[i] <= distance:
                            saved += 1

            return left + right
        
        dfs(root)

        return saved


            




