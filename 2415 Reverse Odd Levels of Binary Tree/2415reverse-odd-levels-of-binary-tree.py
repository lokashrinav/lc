# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        level = 0

        while queue:
            if level % 2:
                for i in range(len(queue) // 2):
                    left, right = queue[i], queue[len(queue) - i - 1]
                    left.val, right.val = right.val, left.val

            for i in range(len(queue)):
                out = queue.popleft()
                if out.left:
                    queue.append(out.left)
                if out.right:
                    queue.append(out.right)
        
            level += 1
        
        return root
