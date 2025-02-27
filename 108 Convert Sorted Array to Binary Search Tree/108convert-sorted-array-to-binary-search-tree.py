# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if right < left:
                return None
            if left == right:
                return TreeNode(nums[left])
            
            mid = (right + left) // 2
            curr = TreeNode(nums[mid])
            curr.left = dfs(left, mid - 1)
            curr.right = dfs(mid + 1, right)
            return curr
        
        return dfs(0, len(nums) - 1)