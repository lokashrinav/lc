# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        count = 0
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
            if count % 2 == 0:
                res.append(lis[::-1])
            else:
                res.append(lis)
            count += 1
        
        return res
        