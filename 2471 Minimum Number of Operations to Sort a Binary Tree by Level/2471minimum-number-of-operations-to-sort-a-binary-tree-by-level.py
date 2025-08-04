# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        '''
        1
        2
        5, 6, 7, 8
        '''

        queue = deque([root])
        total = 0

        while queue:
            curr = list(elem.val for elem in queue)
            curr.sort()
            hmap = {}
            for i in range(len(queue)):
                hmap[queue[i].val] = i
                
            next1 = []
            for i in range(len(queue)):
                out = queue[i]
                if out.left:
                    next1.append(out.left)
                if out.right:
                    next1.append(out.right)
            
            for i in range(len(queue)):
                # print(queue[i].val, curr[i])
                if queue[i].val != curr[i]:
                    hmap[queue[i].val] = hmap[curr[i]]
                    queue[i], queue[hmap[curr[i]]] = queue[hmap[curr[i]]], queue[i]
                    hmap[curr[i]] = i
                    total += 1
                # print([elem.val for elem in queue])
            
            # print(total, curr)

            queue = deque(next1)
        
        return total

        
        