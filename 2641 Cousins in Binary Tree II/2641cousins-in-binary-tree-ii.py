# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = deque([(root, root.val)])

        while queue:
            sum1 = sum(x.val for x, y in queue)
            for i in range(len(queue)):
                out, num1 = queue.popleft()
                out.val = sum1 - num1

                first = 0 if not out.right else out.right.val
                second = 0 if not out.left else out.left.val

                if out.left:
                    queue.append([out.left, first + second])
                
                if out.right:
                    queue.append([out.right, first + second])
        
        return root

        

        