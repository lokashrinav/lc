# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        list1 = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            list1.append(node.val)
            dfs(node.right)
        
        dfs(root)

        l, r = 0, len(list1) - 1

        print(list1)

        while l < r:
            if list1[l] + list1[r] > k:
                r -= 1
            elif list1[l] + list1[r] < k:
                l += 1
            else:
                return True
        
        return False
        