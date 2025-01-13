# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def dfs(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            idk = TreeNode(arr[0])

            i = 1
            while i < len(arr):
                if arr[i] > arr[0]:
                    break
                i += 1
            
            idk.left = dfs(arr[1:i])
            idk.right = dfs(arr[i:])

            return idk

        
        return dfs(preorder)
        