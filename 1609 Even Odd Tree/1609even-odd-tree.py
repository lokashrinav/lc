# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])
        even = 0

        while queue:
            if not even:
                prev = float('-inf')
            else:
                prev = float('inf')

            for i in range(len(queue)):
                node = queue.popleft()
                out = node.val
                if not even:
                    if out % 2 == 0:
                        return False
                    if out <= prev:
                        return False
                else:
                    if out % 2:
                        return False
                    if out >= prev:
                        return False
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                prev = out
            
            even ^= 1

        
        return True
        