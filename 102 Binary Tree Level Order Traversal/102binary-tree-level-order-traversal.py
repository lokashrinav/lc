# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)

        if not root:
            return []
        
        levelOrder = []
        while queue:
            currLength = []
            for i in range(len(queue)):
                q = queue.popleft()
                if not q:
                    continue
                currLength.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            levelOrder.append(currLength)

        return levelOrder
                

        
        