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

        queue = deque([root])
        res = [[]]
        check = 0

        while queue:
            next1 = []
            for i in range(len(queue)):
                out = queue[i]
                if out.left:
                    next1.append(out.left)
                if out.right:
                    next1.append(out.right)

            if check % 2 == 0:
                for i in range(len(queue)):
                    out = queue.popleft()
                    res[-1].append(out.val)
            else:
                for i in range(len(queue)):
                    out = queue.pop()
                    res[-1].append(out.val)

            res.append([])
            queue = deque(next1)
            check += 1
        
        if not res[-1]:
            res.pop()

        return res
            

        