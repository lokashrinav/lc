# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(1, root)])
        maxNum = 0

        while queue:
            for i in range(len(queue)):
                curr, out = queue.popleft()

                if out.left:
                    queue.append((2 * curr, out.left))
                
                if out.right:
                    queue.append((2 * curr + 1, out.right))

            if queue:
                maxNum = max(maxNum, queue[-1][0] - queue[0][0])
        
        return maxNum + 1
        '''
        0, 1
        -1, 3 | 1, 2
        -2, 5 | 0, 3 | 


        

        '''
        