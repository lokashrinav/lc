# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if len(arr) == 1:
                return TreeNode(arr[0])
            if len(arr) == 0:
                return None
 
            maxNum = max(arr)
            maxIndex = arr.index(maxNum)

            idk = TreeNode(maxNum)
            idk.right = dfs(arr[maxIndex + 1:])
            idk.left = dfs(arr[:maxIndex])

            return idk

            
        
        return dfs(nums)
        