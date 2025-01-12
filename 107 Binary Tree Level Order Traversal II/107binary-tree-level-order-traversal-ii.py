# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)        
        res = []
        while queue:
            lis = []
            for i in range(len(queue)):
                out = queue.popleft()
                lis.append(out.val)
                if out.right:
                    queue.append(out.right)
                if out.left:
                    queue.append(out.left)
            res.append(lis[::-1])
        return res[::-1]


        