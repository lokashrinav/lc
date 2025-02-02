# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            elif abs(root.val - target) == abs(closest - target) and root.val < target:
                closest = root.val
            
            root = root.left if root.val > target else root.right
        
        return closest
            